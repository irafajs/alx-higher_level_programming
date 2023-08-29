#!/usr/bin/python3
""" define class named Square """


class Square:
    """defines a function called __init__"""
    def __init__(self, size=0):
        """ if statement"""
        if not isinstance(size, int):
            """raise an error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """raise an error"""
            raise ValueError("size must be >= 0")
        else:
            """Initialize __size with size"""
            self.__size = size
