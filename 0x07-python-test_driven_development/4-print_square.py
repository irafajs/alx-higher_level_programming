#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int) or (not isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for item in range(size):
        print('#' * size)
