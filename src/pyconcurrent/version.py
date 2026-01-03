# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2025-present Gene C <arch@sapience.com>
"""
Project pyconcurrent.
"""

__version__ = "2.11.0"
__date__ = "2026-01-03"
__reldev__ = "release"


def version() -> str:
    """ report version and release date """
    vers = f'pyconcurrent: version {__version__} ({__date__}'
    return vers
