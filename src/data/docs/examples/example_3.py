#!/usr/bin/python
"""
Non-Concurrent
"""
from pyconcurrent import run_prog


def main():
    """
    Run external program with arguments
    """
    pargs_good = ['/usr/bin/sleep', '1']
    pargs_bad = ['/usr/bin/false']

    for pargs in [pargs_good] + [pargs_bad]:
        print(f'Testing: {pargs}:')
        (ret, stdout, stderr) = run_prog(pargs)

        if ret == 0:
            print('\tAll well')
            print(stdout)
        else:
            print('\tFailed')
            print(stderr)


if __name__ == '__main__':
    main()
