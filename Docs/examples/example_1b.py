#!/usr/bin/python
"""
Example 1b
"""
from pyconcurrent import ProcRunMp


def main():
    """
    Multiprocessing
    """
    pargs = ['/usr/bin/sleep']
    tasks = [(1, 1), (2, 7), (3, 2), (4, 2), (5, 1)]

    proc_run = ProcRunMp(pargs, tasks, num_workers=4, timeout=30)
    proc_run.run_all()
    proc_run.print_results()


if __name__ == '__main__':
    main()
