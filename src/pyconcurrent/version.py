# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025-present  Gene C <arch@sapience.com>
"""
Project pyconcurrent.
"""

__version__ = "2.1.0"
__date__ = "2025-04-30"
__reldev__ = "release"


def version() -> str:
    """ report version and release date """
    vers = f'pyconcurrent: version {__version__} ({__date__}'
    return vers
