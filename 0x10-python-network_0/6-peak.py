#!/usr/bin/python3
"""
Shebang to make PY script
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    small, big = 0, len(list_of_integers) - 1
    while small < big:
        mid = (small + big) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            big = mid
        else:
            small = mid + 1
    return list_of_integers[small]
