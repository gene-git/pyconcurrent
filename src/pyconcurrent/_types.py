# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2025-present Gene C <arch@sapience.com>
"""
Some private types.

Used internally.
"""
from enum import Enum


class CallType(Enum):
    """
    Enum indicating subprocess or function.

    :meta private:
    """
    NONE = 0
    FUNCTION = 1
    EXEC = 2


class MPType(Enum):
    """
    Enum indicating via asyncio or multiprocessing.

    :meta private:
    """
    NONE = 0
    ASYNCIO = 1
    MP = 2
