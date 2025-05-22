# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025-present  Gene C <arch@sapience.com>
"""
Run process with timeout.
"""
# pylint: disable=too-many-instance-attributes,too-few-public-methods
# pylint: disable=too-many-arguments,too-many-positional-arguments

from typing import (Any)
import time

from .proc_result import ProcResult
from ._types import (CallType, MPType)
from ._utils import seconds_to_datetime_string


# ----------------------------------------
# Public Class
#   Base Class for both mp and asyncio
#
class ProcRun:
    """
    Parallelization via asyncio / multiprocessing.

    Base Class used by ProcRunMP / ProcRunAsyncio.
    """
    def __init__(self,
                 pargs: list[Any],
                 tasks_todo: list[tuple[Any, Any]],
                 mp_type: MPType,
                 num_workers: int = 4,
                 timeout: int = 0,
                 verb: bool = False):
        """
        Basic Setup ahead of .run_all().
         - tasks_todo is a list of (key, argument)
         - each key must be able to be converted to a string using str(key)
        """
        self.ok = True
        self.verb = verb
        self.num_workers = num_workers
        self.pargs = pargs
        self.tasks_todo = tasks_todo
        self.result: list[ProcResult] = []
        self.timeout = timeout
        self.mp_type = mp_type
        self.call_type: CallType = CallType.EXEC

        # track total run time
        self.time_start = time.time()
        self.time_end: float = -1
        self.time_run: float = -1

        self._prepare()

    def _prepare(self):
        """
        Prepare the work.
        """
        self.call_type = CallType.EXEC
        self.mp_type = MPType.MP
        self.ok = True

        pargs = self.pargs
        if pargs and pargs[0] and callable(pargs[0]):
            self.call_type = CallType.FUNCTION

        if self.num_workers <= 0:
            self.num_workers = 1

    def _check_task_keys_unique(self):
        """
        Check keys are unique
        """
        if not self.tasks_todo:
            return

        unique_keys = set(key for (key, arg) in self.tasks_todo)
        num_unique_keys = len(unique_keys)
        num_keys = len(self.tasks_todo)

        if num_keys != num_unique_keys:
            print('Error : task keys must be unique')
            self.ok = False

    def print_results(self):
        """
        Test tool : prints each result using the ProcResul::print().
        """
        print(10*'*')
        dtm = seconds_to_datetime_string(self.time_start)
        print(f'Test start time : {dtm}')
        print(f' Total run time : {self.time_run:.1f}')
        print('')

        for res in self.result:
            res.print()
