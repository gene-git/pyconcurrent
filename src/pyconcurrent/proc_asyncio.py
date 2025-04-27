# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025-present  Gene C <arch@sapience.com>
"""
Concurrent tasks using asyncio.
"""
# pylint: disable=broad-exception-caught
# pylint: disable=too-many-arguments,too-many-positional-arguments
# pylint: disable=duplicate-code


from typing import (Any, Callable, List, Tuple)
import time
import asyncio

from .proc_result import ProcResult
from ._proc import (ProcRun)
from ._types import (CallType, MPType)


# ----------------------------------------
# Public Class
#
class ProcRunAsyncio(ProcRun):
    """
    Run concurrent processes using asyncio.

    Asynio concurrent process runs. Supports program to be run as a
    subprocess or a function to be called.
    The result of each run is returned as in ProcResult class instance.

    Args:
        pargs ([Any]):
            The first element is the command/function to be run and remainder
            are any additional arguments.

        tasks_todo ([(Any, Any)]):
            List of task items to be run concurrently.
            Each task is a 2-tuple, *(key, arg)*.
            - Key is a unique identifier, converable to string via str(key)
            - arg is an additional argument to the routine when it is called.
            Both key and arg are saved into the result class instance returned.

        num_workers (int):
            Max number of processes to use. Value of 0 is unlimited and 1 will
            mean each is run serially one at a time.

        timeout (int):
            The maximum number of seconds allotted to each process.
            If not complete within "timeout", then process/function
            will be cancelled/killed and the "result" instance will include:
            - res.success set to *False*
            - res.timeout set to *True*.

        verb (bool):
            If set to true, some additional information is sent to stdout.

    Attributes:
        result (*[ProcResult]*):
            List of results, one per task. See ProcResult for more detail.

    Methods:

    """
    def __init__(self,
                 pargs: List[Any],
                 tasks_todo: List[Tuple[Any, Any]],
                 num_workers: int = 4,
                 timeout: int = 0,
                 verb: bool = False):

        super().__init__(pargs, tasks_todo, MPType.ASYNCIO, num_workers,
                         timeout, verb)

    async def _do_one_task_func(self, semaphore: asyncio.locks.Semaphore,
                                key: Any, arg: Any):
        """
        Private: Call one instance of a function pargs[0](pargs[1:] + [arg]).

         - function must return a tupple:
            (success:bool, Any)
         - Exceptions func() may raise:
           RuntimeError
           timeout is ignored in this routine.
        """
        if self.verb:
            print(f' _do_one_task_func {key} {arg} {self.timeout}')

        pargs = self.pargs
        res = ProcResult(key, arg)

        func = pargs[0]
        args = []
        if len(pargs) > 1:
            args = pargs[1:]
        args += [arg]

        timeout = self.timeout if self.timeout > 0 else None
        async with semaphore:
            async with asyncio.timeout(timeout):
                try:
                    (success, answer) = await func(key, args)
                    res.success = success
                    res.answer = answer
                    res.timeout = True

                except (RuntimeError, asyncio.CancelledError) as err:
                    res.success = False
                    res.timeout = True
                    res.exception = type(err).__name__

                except (KeyboardInterrupt, SystemExit) as err:
                    res.success = False
                    res.exception = type(err).__name__

                except TimeoutError as err:
                    res.success = False
                    res.timeout = True
                    res.exception = type(err).__name__

        res.time_end = time.time()
        res.time_run = res.time_end - res.time_start
        return res

    async def _do_one_task_exec(self, semaphore: asyncio.locks.Semaphore,
                                key: Any, arg: Any):
        """
        Private: Run one instance pargs + [arg].
        """
        if self.verb:
            print(f'_do_one_task_exec {key} {arg} {self.timeout}')

        res = ProcResult(key, arg)
        pargs = self.pargs + [arg]
        pargs_str = [str(one) for one in pargs]

        pipe = asyncio.subprocess.PIPE
        timeout = self.timeout if self.timeout > 0 else None
        async with semaphore:
            try:
                proc = await asyncio.create_subprocess_exec(*pargs_str,
                                                            stdout=pipe,
                                                            stderr=pipe,
                                                            )

                try:
                    async with asyncio.timeout(timeout):
                        await proc.communicate()

                except TimeoutError as err:
                    proc.kill()
                    res.success = False
                    res.timeout = True
                    res.exception = type(err).__name__

                except (RuntimeError, asyncio.CancelledError) as err:
                    res.success = False
                    res.exception = type(err).__name__

                except (KeyboardInterrupt, SystemExit) as err:
                    res.success = False
                    res.exception = type(err).__name__

                finally:
                    res.time_end = time.time()
                    res.time_run = res.time_end - res.time_start
                    res.returncode = proc.returncode

                    if proc.returncode is None:
                        proc.kill()
                        res.success = False
                        res.timeout = True

                    elif proc.returncode == 0:
                        res.success = True

                    if proc.stdout:
                        data = await proc.stdout.read()
                        if data:
                            res.stdout = data.decode('utf-8')

                    if proc.stderr:
                        data = await proc.stderr.read()
                        if data:
                            res.stderr = data.decode('utf-8')

            except (FileNotFoundError, PermissionError, OSError) as err:
                res.success = False
                res.exception = type(err).__name__

        return res

    def _get_do_one_task(self) -> Callable:
        """
        Private: Return the method to use for each run.

         - run a function
         - exec a subprocess.
        """
        match self.call_type:
            case CallType.FUNCTION:
                return self._do_one_task_func

            case CallType.EXEC:
                return self._do_one_task_exec

            case _:     # should never get here - added to keep mypy happy.
                return self._do_one_task_exec

    async def _run_taskgroup(self):
        """
        Private: Run using asyncio.
        """
        semaphore = asyncio.Semaphore(self.num_workers)
        do_one_task = self._get_do_one_task()

        tasklist = []
        try:
            async with asyncio.TaskGroup() as grp:
                for todo in self.tasks_todo:
                    task_name = str(todo[0])
                    task = grp.create_task(do_one_task(semaphore, *todo))
                    task.set_name(task_name)
                    tasklist.append(task)

        except ExceptionGroup as _err:
            if self.verb:
                print(f'Exception: {_err}')
            # pass

        #
        # results from tasklist
        #
        self.result = []
        for task in tasklist:
            result = task.result()
            if result:
                self.result.append(result)

    async def run_all(self):
        """
        Start running all the provided commands/functions concurrently.

        Awaitable, so caller is responsible for calling asyncio.run().
        See run_all_start_asyncio() for non-awaitable version.
        """
        if not self.ok:
            print('Error - unable to run')
            return

        # timer for entire run
        self.time_start = time.time()

        await self._run_taskgroup()

        self.time_end = time.time()
        self.time_run = self.time_end - self.time_start
