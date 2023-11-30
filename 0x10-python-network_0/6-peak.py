#!/usr/bin/python3
"""
Shebang to make PY script
"""


def find_peak(list_of_integers):
    list_sz = len(list_of_integers)
    if list_sz == 0:
        return None
    bigger = list_of_integers[0]
    for count in range(list_sz - 1):
        if list_of_integers[count] > list_of_integers[count + 1]:
            bigger = list_of_integers[count]
        else:
            bigger = list_of_integers[count + 1]
    return bigger
