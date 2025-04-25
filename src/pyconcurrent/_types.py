# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025-present  Gene C <arch@sapience.com>
'''
Some private types
Only used internally
'''
from enum import Enum

class CallType(Enum):
    '''
    subprocess or function
    :meta private:
    '''
    NONE = 0
    FUNCTION = 1
    EXEC = 2

class MPType(Enum):
    '''
    via asyncio or multiprocessing
    :meta private:
    '''
    NONE = 0
    ASYNCIO = 1
    MP = 2
