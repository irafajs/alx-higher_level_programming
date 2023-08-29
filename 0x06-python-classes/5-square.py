#!/usr/bin/python3
"""defines class named Square"""


class Square:
    """defines a function called __init__"""
    def __init__(self, size=0):
        """initialize size to size"""
        self.size = size

    """defines a function called size"""
    @property
    def size(self):
        """returns size"""
        return self.__size
    """define a function called size with 2 objects"""
    @size.setter
    def size(self, value):
        """if statement"""
        if not isinstance(value, int):
            """raise an error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """raise an error"""
            raise ValueError("size must be >= 0")
        else:
            """initialize __size with value"""
            self.__size = value
    """defines a public function called area"""
    def area(self):
        """return power of 2 of __size"""
        return self.__size ** 2
    """defines a public function called my_print"""
    def my_print(self):
        """if statement"""
        if self.__size == 0:
            """print function to print empty line"""
            print()
        else:
            """for loop statement"""
            for i in range(self.__size):
                """print function to print a square of # symbol"""
                print("#" * self.__size)

