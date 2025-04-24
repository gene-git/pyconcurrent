# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025-present  Gene C <arch@sapience.com>
"""
Project pyconcurrent
"""

__version__ = "1.1.3"
__date__ = "2025-04-24"
__reldev__ = "release"

def version() -> str:
    """ report version and release date """
    vers = f'python-parallel: version {__version__} ({__date__}'
    return vers
