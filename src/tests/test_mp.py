"""
Test :
    ProcRunMp class using subprocesses.
"""
# pylint: disable=duplicate-code,too-few-public-methods
from typing import (Any)
import time

from pyconcurrent import ProcRunMp              # noqa: E402


def _func_mp(key, args) -> tuple[bool, dict[str, Any]]:
    """
    Async test function.
    """
    success = True
    nap = args[-1]
    time.sleep(nap)

    answer = {
            'key': key,
            'args': args,
            'success': success,
            'result': 'test_func done',
            }

    return (success, answer)


class _TestData:
    """ container for test data """
    def __init__(self, pargs, tasks, timeout, num):
        """ set up the test """
        self.pargs = pargs
        self.tasks = tasks
        self.timeout = timeout
        self.num = num
        self.time_max = self.timeout + sum(x[1] for x in self.tasks)
        self.all_ok = False


class TestMp:
    """
    Tests ProcRunMp with and without a timeout case.
    """

    def _result(self, tdata, prun, num_success_target):
        """ finalize and get result """
        num_success = sum(res.success for res in prun.result)
        time_taken = sum(res.time_run for res in prun.result)
        all_ok = (num_success == num_success_target and
                  time_taken <= tdata.time_max
                  )
        return all_ok

    def test_mp_subprocess(self):
        """
        Subprocess test without timeout being hit.
        """
        pargs = ['/usr/bin/sleep']
        tasks = [(1, 1), (2, 4), (3, 2)]
        timeout = 10
        num = 5
        tdata = _TestData(pargs, tasks, timeout, num)

        prun = ProcRunMp(pargs, tasks, num_workers=num, timeout=timeout)
        prun.run_all()

        num_success_target = len(tasks)
        all_ok = self._result(tdata, prun, num_success_target)
        assert all_ok

    def test_mp_subprocess_timeout(self):
        """
        Subprocess test with timeout being hit once.
        """
        pargs = ['/usr/bin/sleep']
        tasks = [(1, 1), (2, 10), (3, 2)]
        timeout = 5
        num = 5
        tdata = _TestData(pargs, tasks, timeout, num)

        prun = ProcRunMp(pargs, tasks, num_workers=num, timeout=timeout)
        prun.run_all()

        num_success_target = len(tasks) - 1
        all_ok = self._result(tdata, prun, num_success_target)
        assert all_ok

    def test_mp_func(self):
        """
        Function test without timeout being hit.
        """
        pargs = [_func_mp, 'dummy1']
        tasks = [(1, 1), (2, 4), (3, 2)]
        timeout = 10
        num = 5
        tdata = _TestData(pargs, tasks, timeout, num)

        prun = ProcRunMp(pargs, tasks, num_workers=num, timeout=timeout)
        prun.run_all()

        num_success_target = len(tasks)
        all_ok = self._result(tdata, prun, num_success_target)
        assert all_ok

    def test_mp_func_timeout(self):
        """
        Function test with 1 timeout being hit.
        """
        pargs = [_func_mp, 'dummy1']
        tasks = [(1, 1), (2, 10), (3, 2)]
        timeout = 5
        num = 5
        tdata = _TestData(pargs, tasks, timeout, num)

        prun = ProcRunMp(pargs, tasks, num_workers=num, timeout=timeout)
        prun.run_all()

        num_success_target = len(tasks)
        all_ok = self._result(tdata, prun, num_success_target)
        assert all_ok
