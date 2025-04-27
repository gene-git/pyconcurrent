# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025-present  Gene C <arch@sapience.com>
"""
Concurrent tasks using multiprocessing.
"""
# pylint: disable=broad-exception-caught
# pylint: disable=too-many-arguments,too-many-positional-arguments
# pylint: disable=consider-using-with
# pylint: disable=duplicate-code

from typing import (Any, Callable, List, Tuple)
import time
import subprocess
import multiprocessing

from ._types import (CallType, MPType)
from ._proc import (ProcRun)
from .proc_result import ProcResult


# ----------------------------------------
# Public Class
#
class ProcRunMp(ProcRun):
    """
    Run concurrent processes using multiprocessing.

    Same calling convention as ProcRunAsyncio.

    Note: func cannot be async func() - conflicts with mp starmap using async

    """
    _start_method_set = False

    def __init__(self,
                 pargs: List[Any],
                 tasks_todo: List[Tuple[Any, Any]],
                 num_workers: int = 4,
                 timeout: int = 0,
                 verb: bool = False):
        """
        Basic Setup ahead of .run_all()
        """
        super().__init__(pargs, tasks_todo, MPType.MP, num_workers,
                         timeout, verb)

        if not ProcRunMp._start_method_set:
            multiprocessing.set_start_method('spawn', force=True)
            ProcRunMp._start_method_set = True

    def _get_task_one(self) -> Callable:
        """
        Private: Run one instance pargs + [arg]

        Wrapper for MP. Handles func() and subprocess
        """
        match self.call_type:
            case CallType.FUNCTION:
                return self._task_one_func

            case CallType.EXEC:
                return self._task_one_exec

            case _:
                return self._task_one_exec

    def _task_one_func(self, key, arg):
        """
        Private: Call one instance of a function pargs[0](pargs[1:] + [arg]).

         - function must return a tupple:
            (success:bool, Any)
         - Exceptions func() may raise:
           RuntimeError
           timeout is ignored in this routine.
        """
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
            (success, answer) = func(key, args)
            res.success = success
            res.answer = answer

        except RuntimeError as err:
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

    def _task_one_exec(self, key, arg):
        """
        Private: Run one instance pargs + [arg].

        Wrapper for MP. Handles func() and subprocess.
        """
        if self.verb:
            print(f'task_one {key} {arg} {self.timeout}')
        res = ProcResult(key, arg)

        pargs = self.pargs + [arg]
        pargs_str = [str(one) for one in pargs]

        try:
            ret = subprocess.run(pargs_str,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 check=False,
                                 timeout=self.timeout
                                 )

            res.time_end = time.time()
            res.time_run = res.time_end - res.time_start

            res.returncode = ret.returncode
            if ret.returncode == 0:
                res.success = True

            if ret.stdout:
                res.stdout = ret.stdout.decode()

            if ret.stderr:
                res.stderr = ret.stderr.decode()

        except subprocess.TimeoutExpired:
            res.success = False
            res.timeout = True

        except (FileNotFoundError, PermissionError, OSError):
            res.success = False

        except Exception:
            # catch all
            res.success = False

        return res

    def _run_one_at_a_time(self):
        """
        Private: Run one at a time.

           Can also change to call subprocess directly.
        """
        task_one = self._get_task_one()
        for task in self.tasks_todo:
            res = task_one(*task)
            self.result.append(res)

    def _run_mp(self):
        """
        Private: Run using mp.

            func = func(common:[str], key:str, arg:str).
        """
        task_one = self._get_task_one()
        pool = multiprocessing.Pool(processes=self.num_workers)
        self.result = pool.starmap(task_one, self.tasks_todo)
        pool.close()

    def run_all(self):
        """
        Do the work
        """
        if not self.ok:
            print('Error - unable to run')
            return

        # timer for entire run
        self.time_start = time.time()

        if self.num_workers < 2:
            self._run_one_at_a_time()
        else:
            self._run_mp()

        self.time_end = time.time()
        self.time_run = self.time_end - self.time_start
