#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Find peak
    """
    _list = list_of_integers[:]
    length = len(_list)
    if length == 0:
        return
    first_peak = _list[0]
    peak = _list[0]
    for i in range(length - 1):
        if (_list[i] >= _list[i + 1] and _list[i] >= _list[i - 1]):
            peak = _list[i]
    if first_peak > peak:
        peak = first_peak
    return peak
    """
    if len(list_of_integers) > 1:
        return max(list_of_integers)
    return
    """
