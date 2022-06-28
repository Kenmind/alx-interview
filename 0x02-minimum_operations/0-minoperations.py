#!/usr/bin/python3
"""Defines minOperations"""


def minOperations(n):
    """Performs minOperations on n and
    returns the total number of performed operations to achieve n"""
    if not isinstance(n, int) or n < 2:
        return 0

    _times: int = 0
    _copied: int = 0
    _max: int = 1

    while _max < n:
        if _copied == 0:
            _copied = _max
            _max += _copied
            _times += 2

        elif (n - _max) > 0 and (n - _max) % _max == 0:
            _copied = _max
            _max += _copied
            _times += 2

        elif _copied > 0:
            _max += _copied
            _times += 1

    return _times
