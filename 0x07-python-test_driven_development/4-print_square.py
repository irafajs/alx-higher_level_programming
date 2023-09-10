#!/usr/bin/python3
"""__doc__"""


def print_square(size):
    """function to print square"""
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for item in range(size):
        print('#' * size)
