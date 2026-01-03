# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2025-present Gene C <arch@sapience.com>
"""
Shared tools.
"""
import datetime
from dateutil import parser as date_parser
from dateutil import tz


def get_datetime_now() -> datetime.datetime:
    """
    Get current date time.
    """
    dtm = datetime.datetime.now(tz.tzlocal())
    return dtm


def get_reltime(date_str: str, now: datetime.datetime) -> int:
    """
    Get relative time in seconds.

     return now - date.
    """
    if not date_str:
        return -1

    date = date_parser.parse(date_str)
    delta = now - date
    seconds = delta.seconds
    return seconds


def fmt_seconds(secs: int) -> str:
    """
    format output given seconds.
    """
    hour = int(secs // 3600)
    secs %= 3600

    #
    # days = int(hour // 24)
    # hour %= 24
    #

    mins = int(secs // 60)
    secs %= 60

    hfmt = f'{hour:02d}:' if hour > 0 else f'{"":3s}'
    mfmt = f'{mins:02d}:' if mins > 0 else f'{"":3s}'

    dtf = f'{hfmt}{mfmt}{secs:04.1f}'
    return dtf


def seconds_to_datetime_string(seconds: float) -> str:
    """
    Convert seconds to human.
    """
    dtime = datetime.datetime.fromtimestamp(seconds)
    dtime_str = dtime.strftime('%Y-%m-%d %H:%M:%S')
    return dtime_str
