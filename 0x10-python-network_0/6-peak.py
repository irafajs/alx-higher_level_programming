#!/usr/bin/python3
"""
Shebang to make PY script
"""


def find_peak(list_of_integers):
    listoi = list_of_integers
    if not listoi:
        return None
    small, big = 0, len(listoi) - 1
    while small < big:
        mid = (small + big) // 2
        if listoi[mid] >= listoi[mid + 1] and listoi[mid] >= listoi[mid - 1]:
            big = mid
        if listoi[mid] < listoi[mid + 1]:
            small = mid + 1
        else:
            big = mid
    return listoi[small]
