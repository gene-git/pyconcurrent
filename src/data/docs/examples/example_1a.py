#!/usr/bin/python
"""
Example 1
"""
import asyncio
from pyconcurrent import ProcRunAsyncio


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
