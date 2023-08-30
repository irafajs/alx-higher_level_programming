#!/usr/bin/python3
"""defines class named Square"""


class Square:
    """defines a function called __init__"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize size to size"""
        self.size = size
        """initialize position to position"""
        self.position = position

    """defines a function called size"""
    @property
    def size(self):
        """return __size"""
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
            """initialize __size to value"""
            self.__size = value
    """defines a function called position"""
    @property
    def position(self):
        """return __position"""
        return self.__position
    """defines function called position with 2 objects"""
    @position.setter
    def position(self, value):
        """if statement"""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or not all(isinstance(i, int)
            for i in value) or
            value[0] < 0 or value[1] < 0
        ):
            """raise ar error"""
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            """initialize __position to value"""
            self.__position = value
    """defines a function called area"""
    def area(self):
        """return square of __size"""
        return self.__size ** 2
    """defines a function called print"""
    def my_print(self):
        """if statement"""
        if self.__size == 0:
            """print a blank line"""
            print()
        else:
            """for statement"""
            for _ in range(self.__position[1]):
                """print a blank line"""
                print()
                """for statement"""
            for _ in range(self.__size):
                """print the expected outpu"""
                print(" " * self.__position[0] + "#" * self.__size)
