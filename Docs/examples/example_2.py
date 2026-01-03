#!/usr/bin/python
"""
Example 2
"""
import asyncio
from typing import Any
from pyconcurrent import ProcRunAsyncio


async def test_func_async(key, args) -> tuple[bool, dict[str, Any]]:
    """
    return 2-tuple (success, result).
    """
    success = True
    nap_time = args[-1]     # pull off the last argument

    await asyncio.sleep(nap_time)
    answer: dict[str, Any] = {
            'key': key,
            'args': args,
            'success': success,
            'result': 'test_func done',
            }
    return (success, answer)


async def main():
    """
    pargs can have additional arguments.
    """
    pargs = ['/usr/bin/sleep']
    tasks = [(1, 1), (2, 7), (3, 2), (4, 2), (5, 1)]

    proc_run = ProcRunAsyncio(pargs, tasks, num_workers=4, timeout=30)
    await proc_run.run_all()
    proc_run.print_results()


if __name__ == '__main__':
    asyncio.run(main())
