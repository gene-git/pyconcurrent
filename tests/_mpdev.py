#!/usr/bin/python
'''
Test harness for ProcRunn
 - test running program:
    - mtype = 'serial' or num_workers = 1
      run in serial one at a time
    - mtype = 'asyncio'
      subprocesses using asyncio
    - mtype = 'mp'
      subprocesses using multiprocessing threads
      or calling function if pargs[0] is a function instead of command to run
    - NB asyncio with function not supported yet - only subprocesses
'''
# pylint: disable=too-many-branches,wrong-import-position
from dataclasses import dataclass
import os
import sys
import time
import asyncio

parent_dir = os.path.abspath('../src')
sys.path.insert(0, parent_dir)

from pyconcurrent import ProcRunMp
from pyconcurrent import ProcRunAsyncio

def test_func_mp(key, args) -> (bool, []):
    '''
    Must return 2-tuple (success, result)
    '''
    success = True
    nap = args[-1]
    time.sleep(nap)

    answer = {
                'key' : key,
                'args' : args,
                'success' : success,
                'result' : 'test_func done',
              }

    return (success, answer)

async def test_func_async(key, args) -> (bool, []):
    '''
    Must return 2-tuple (success, result)
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

def test_subprocess_mp(num_workers:int=5, timeout:int=30):
    ''' test subprocess mp '''
    print(' ======= subprocess mp ========')
    pargs = ['/usr/bin/sleep']
    tasks = [(1, 1), (2,7), (3,2), (4, 2), (5, 1)]

    runner = ProcRunMp(pargs, tasks, num_workers=num_workers, timeout=timeout)
    runner.run_all()
    runner.print_results()
    print('----------------')

async def test_subprocess_asyncio(num_workers:int=5, timeout:int=30):
    ''' test subprocess '''
    print(' ======= subprocess asyncio  ========')
    pargs = ['/usr/bin/sleep']
    tasks = [(1, 1), (2,7), (3,2), (4, 2), (5, 1)]
    runner = ProcRunAsyncio(pargs, tasks, num_workers=num_workers, timeout=timeout)
    await runner.run_all()
    runner.print_results()
    print('----------------')

async def test_function_asyncio(num_workers:int=5, timeout:int=30):
    ''' test function version '''
    print(' ======= function asyncio ========')
    pargs = [test_func_async, "arg1"]
    tasks = [(1, 1), (2,4), (3,2), (4, 2), (5, 1)]

    runner = ProcRunAsyncio(pargs, tasks, num_workers=num_workers, timeout=timeout, verb=True)
    await runner.run_all()
    runner.print_results()
    print('----------------')

async def test_function_mp(num_workers:int=5, timeout:int=30):
    ''' test function version '''
    print(' ======= function asyncio ========')
    pargs = [test_func_mp, "arg1"]
    tasks = [(1, 1), (2,4), (3,2), (4, 2), (5, 1)]

    runner = ProcRunMp(pargs, tasks, num_workers=num_workers, timeout=timeout, verb=True)
    await runner.run_all()
    runner.print_results()
    print('----------------')

@dataclass
class Tests:
    ''' choice of tests to run '''
    asyncio : True
    exec_sub : True
    function : True
    mp : True
    notimeout : True
    serial : True
    timeout : True

def _what_to_test() -> Tests:
    '''
    defaults to all - really dumb just takes a string of first letters of test

    e.g. aen    = asyncio exec_sub notimeout
    '''
    tests = Tests(asyncio=True,
                  exec_sub=True,
                  function=True,
                  mp=True,
                  notimeout=True,
                  serial=True,
                  timeout=True,
                  )
    if len(sys.argv) == 1:
        return tests

    opt = sys.argv[1]
    tests.asyncio = 'a' in opt
    tests.exec_sub = 'e' in opt
    tests.function = 'f' in opt
    tests.mp = 'm' in opt
    tests.notimeout = 'n' in opt
    tests.serial = 's' in opt
    tests.timeout = 't' in opt

    return tests


async def main():
    '''
    Simple test using sleep (better is a program with actual output)
    '''
    #
    # pargs = [command, arg1, arg2, ... ]
    # tasks is list of 2-tuple of (key, argument)
    # key is a unique identifier meaningful to caller for each task
    # Them program is called with argument appended
    #   [command, arg1, arg2, .., argument]
    #
    # mants = mp, async, notimeout, timeout, serial
    #
    breakpoint()
    tests = _what_to_test()

    if tests.mp:
        if tests.exec_sub and tests.notimeout:
            test_subprocess_mp(num_workers=5, timeout=30)

        if tests.exec_sub and tests.serial:
            test_subprocess_mp(num_workers=1, timeout=30)

        if tests.exec_sub and tests.timeout:
            test_subprocess_mp(num_workers=5, timeout=5)

        if tests.function and tests.notimeout:
            test_function_mp(num_workers=5, timeout=0)

        if tests.function and tests.timeout:
            test_function_mp(num_workers=5, timeout=5)

        if tests.function and tests.serial:
            test_function_mp(num_workers=1, timeout=30)

    if tests.asyncio:
        if tests.exec_sub and tests.notimeout:
            await test_subprocess_asyncio(num_workers=5, timeout=30)

        if tests.exec_sub and tests.timeout:
            await test_subprocess_asyncio(num_workers=5, timeout=5)

        if tests.exec_sub and tests.serial:
            await test_subprocess_asyncio(num_workers=1, timeout=30)

        if tests.function and tests.notimeout:
            await test_function_asyncio(num_workers=5, timeout=0)

        if tests.function and tests.timeout:
            await test_function_asyncio(num_workers=5, timeout=5)

        if tests.function and tests.serial:
            await test_function_asyncio(num_workers=1, timeout=30)

if __name__ == '__main__':
    asyncio.run(main())
