'''
Test :
    ProcRunAsyncio class using subprocesses
'''
# pylint: disable=wrong-import-position,attribute-defined-outside-init
# pylint: disable=duplicate-code
import os
import sys
import asyncio
import pytest

parent_dir = os.path.abspath('../src')
sys.path.append(parent_dir)
from pyconcurrent import ProcRunAsyncio

async def _func_async(key, args) -> (bool, []):
    '''
    Async test function
    '''
    success = True
    nap = args[-1]
    await asyncio.sleep(nap)

    answer = {
                'key' : key,
                'args' : args,
                'success' : success,
                'result' : 'test_func done',
              }

    return (success, answer)

class TestAsyncio:
    '''
    Tests ProcRunAsyncio with and without a timeout case
    '''
    def _prepare(self, pargs, tasks, timeout, num):
        ''' set up the test '''
        self.pargs = pargs
        self.tasks = tasks
        self.timeout = timeout
        self.num = num
        self.time_max = self.timeout + sum(x[1] for x in self.tasks)
        self.all_ok = False

    def _result(self, prun, num_success_target):
        ''' finalize and get result '''
        num_success = sum(res.success for res in prun.result)
        time_taken = sum(res.time_run for res in prun.result)
        self.all_ok = (num_success == num_success_target) and (time_taken <= self.time_max)
        return self.all_ok

    @pytest.mark.asyncio
    async def test_asyncio_subprocess(self):
        '''
        Subprocess test without timeout being hit
        '''
        pargs = ['/usr/bin/sleep']
        tasks =  [(1, 1), (2,4), (3,2)]
        timeout = 10
        num = 5
        self._prepare(pargs, tasks, timeout, num)

        prun = ProcRunAsyncio(pargs, tasks, num_workers=num, timeout=timeout)
        await prun.run_all()

        num_success_target = len(tasks)
        all_ok = self._result(prun, num_success_target)
        assert all_ok

    @pytest.mark.asyncio
    async def test_asyncio_subprocess_timeout(self):
        '''
        Subprocess test with timeout being hit once
        '''
        pargs = ['/usr/bin/sleep']
        tasks =  [(1, 1), (2,10), (3,2)]
        timeout = 5
        num = 5
        self._prepare(pargs, tasks, timeout, num)

        prun = ProcRunAsyncio(pargs, tasks, num_workers=num, timeout=timeout)
        await prun.run_all()

        num_success_target = len(tasks) - 1
        all_ok = self._result(prun, num_success_target)
        assert all_ok

    @pytest.mark.asyncio
    async def test_asyncio_func(self):
        '''
        Function test without timeout being hit
        '''
        pargs = [_func_async, 'dummy1']
        tasks =  [(1, 1), (2,4), (3,2)]
        timeout = 10
        num = 5
        self._prepare(pargs, tasks, timeout, num)

        prun = ProcRunAsyncio(pargs, tasks, num_workers=num, timeout=timeout)
        await prun.run_all()

        num_success_target = len(tasks)
        all_ok = self._result(prun, num_success_target)
        assert all_ok

    @pytest.mark.asyncio
    async def test_asyncio_func_timeout(self):
        '''
        Function test with 1 timeout being hit
        '''
        pargs = [_func_async, 'dummy1']
        tasks =  [(1, 1), (2,10), (3,2)]
        timeout = 5
        num = 5
        self._prepare(pargs, tasks, timeout, num)

        prun = ProcRunAsyncio(pargs, tasks, num_workers=num, timeout=timeout)
        await prun.run_all()

        num_success_target = len(tasks)
        all_ok = self._result(prun, num_success_target)
        assert all_ok
