# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025-present  Gene C <arch@sapience.com>
'''
Run process with timeout
'''
# pylint: disable=too-many-instance-attributes,too-few-public-methods

from typing import Any
import time

class ProcResult:
    '''
    Result of running one of the concurrent processes.
    
    Args:
        key (Any): 
            Caller provided unique identifier.
        arg (Any): 
            The additional argument used for this run.

    Attributes:
        time_start (float): 
            Unix time in seconds.
        time_run (float): 
            Seconds taken for this item to complete.
        success (bool): 
            True if completed successfully.
        timeout (bool): 
            True if process failed to completed in less than timeout restriction.
        key (Any): 
            The caller provided unique identifier.
        arg (Any): 
            The called provided argument for this run.
        returncode (int): 
            Return value of subprocess. Typically 0 for success.
        stdout (str): 
            Returned stdout of subprocess.
        stderr (str): 
            Returned stderr of subprocess.
        answer (Any): 
            Return provided by the function.

    '''
    def __init__(self, key, arg):
        self.time_start = time.time()
        self.time_end : float = -1
        self.time_run : float = -1
        self.success : bool = False
        self.timeout : bool = False
        self.key = key
        self.arg = arg
        self.returncode : int = -1
        self.stdout : str = None
        self.stderr : str = None
        self.answer : Any = None        # function returns (success, answer)

    def print(self):
        ''' Testing: simple print attributes '''
        print('========================================')
        print(f'key                 : {self.key}')
        print(f'  time_start        : {self.time_start:.1f}')
        print(f'  time_run          : {self.time_run:.1f}')
        print(f'  success           : {self.success}')
        print(f'  timeout           : {self.timeout}')
        print(f'  arg               : {self.arg}')
        print(f'  returncode        : {self.returncode}')
        if self.stdout:
            print(f'  stdout            : {self.stdout}')
        if self.stderr:
            print(f'  stderr            : {self.stderr}')
        if self.answer:
            print(f'  answer            : {self.answer}')
