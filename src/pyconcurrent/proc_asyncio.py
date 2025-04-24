'''
Concurrent tasks using asyncio.
'''
# pylint: disable=broad-exception-caught
# pylint: disable=too-many-arguments,too-many-positional-arguments
# pylint: disable=duplicate-code

from typing import (Any, Callable)
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

from .proc_result import ProcResult
from ._proc import (ProcRun)
from ._types import (CallType, MPType)


# ----------------------------------------
# Public Class
#
class ProcRunAsyncio(ProcRun):
    '''
    Run concurrent processes using asyncio.

    Asynio concurrent process runs. Supports program to be run as a subprocess or a function to be called.
    The result of each run is returned as in ProcResult class instance. 

    Args:
        pargs ([Any]): 
            The first element is the command/function to be run and remainder
            are any additional arguments. 
        tasks ([(Any, Any)]): 
            List of task items to be run concurrently. 
            Each task is a 2-tuple, *(key, arg)*.
            Key is a unique identifier for this run. arg is an additional argument
            to the routine when it is called.  Both key and arg are saved 
            into the result class instance returned.
        num_workers (int): 
            Max number of processes to use. Value of 0 is unlimited and 1 will
            mean each is run serially one at a time.
        timeout (int): 
            Applies to commands run as subprocesses. The maximum number of seconds allotted
            to each process. If not complete, then process will be killed and the result
            will have res.success set to *False* and res.timeout set to *True*.
        verb (bool): 
            If set to true, some additional information is sent to stdout.

    Attributes:
        result (*[ProcResult]*): 
            A list of results, one per item run. See ProcResult for details what is provided.

    Methods:

    '''
    def __init__(self,
                 pargs:[Any],
                 tasks:[(Any, Any)],
                 num_workers:int=4,
                 timeout:int=0,
                 verb:bool=False):
        super().__init__(pargs, tasks, MPType.ASYNCIO, num_workers, timeout, verb)

        if self.num_workers > 0:
            loop = asyncio.get_running_loop()
            loop.set_default_executor(ThreadPoolExecutor(max_workers=self.num_workers))

    async def _task_one_func(self, key, arg):
        '''
        Call one instance of a function pargs[0](pargs[1:] + [arg])
         - function must return a tupple:
            (success:bool, Any)
         - Exceptions func() may raise:
           RuntimeError
           timeout is ignored in this routine.
        '''
        if self.verb:
            print(f' _task_one_func {key} {arg} {self.timeout}')

        pargs = self.pargs
        res = ProcResult(key, arg)

        func = pargs[0]
        args = []
        if len(pargs) > 1:
            args = pargs[1:]
        args += [arg]

        try:
            (success, answer) = await func(key, args)
            res.success = success
            res.answer = answer

        except RuntimeError:
            res.success = False
            res.timeout = True

        res.time_end = time.time()
        res.time_run = res.time_end - res.time_start
        return res

    async def _task_one_exec(self, key, arg):
        '''
        Run one instance pargs + [arg]
        '''
        if self.verb:
            print(f'_task_one_exec {key} {arg} {self.timeout}')

        res = ProcResult(key, arg)
        pargs = self.pargs + [arg]
        pargs_str = [str(one) for one in pargs]

        try:
            proc = await asyncio.create_subprocess_exec(*pargs_str,
                                                        stdout=asyncio.subprocess.PIPE,
                                                        stderr=asyncio.subprocess.PIPE,
                                                        )

            timeout = self.timeout if self.timeout > 0 else None
            res.stdout, res.stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)

            res.time_end = time.time()
            res.time_run = res.time_end - res.time_start
            res.returncode = proc.returncode
            if proc.returncode == 0:
                res.success = True

        except asyncio.TimeoutError:
            proc.kill()
            res.success = False
            res.timeout = True

        except (FileNotFoundError,PermissionError, OSError) :
            res.success = False

        except Exception :
            # catch all
            res.success = False

        return res

    def _get_task_one(self) -> Callable:
        '''
        Return the method to use for each run
         - run a function
         - exec a subprocess
        '''
        match self.call_type :
            case CallType.FUNCTION:
                return self._task_one_func

            case CallType.EXEC:
                return self._task_one_exec

    async def _run_one_at_a_time(self):
        '''
        Run : one at a time
         - task = (key, arg)
        '''
        task_one = self._get_task_one()
        for task in self.tasks:
            res = await task_one(*task)
            self.result.append(res)

    async def _run_gather(self):
        '''
        Run using asyncio
        '''
        task_one = self._get_task_one()
        tasks = [task_one(*task) for task in self.tasks]
        self.result = await asyncio.gather(*tasks)

    async def run_all(self):
        '''
        Start running all the provided commands/functions concurrently.
        '''
        if not self.ok:
            print('Error - unable to run')
            return

        # timer for entire run
        self.time_start = time.time()

        if self.num_workers < 2:
            await self._run_one_at_a_time()
        else :
            await self._run_gather()

        self.time_end = time.time()
        self.time_run = self.time_end - self.time_start
