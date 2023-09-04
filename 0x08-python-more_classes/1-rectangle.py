#!/usr/bin/python3
"""defines class named Rectangle"""


class Rectangle:
    """defines a function called __init__"""
    def __init__(self, width=0, height=0):
        """initialize width to width"""
        self.width = width
        """initialize height to height"""
        self.height = height

    """defines a function called width"""
    @property
    def width(self):
        """return size"""
        return self.__width
    """defines a function called width used as a setter"""
    @width.setter
    def width(self, value):
        """if statement block"""
        if not isinstance(value, int):
            """raise an error"""
            raise TypeError("width must be an integer")
        elif value < 0:
            """raise an error"""
            raise ValueError("width must be >= 0")
        else:
            """initiate private value __width"""
            self.__width = value
    """defines a function named height"""
    @property
    def height(self):
        """return private variable __height"""
        return self.__height
    """defines a function named height to set the fields"""
    @height.setter
    def height(self, value):
        """if statement block"""
        if not isinstance(value, int):
            """raise an error"""
            raise TypeError("height must be an integer")
        elif value < 0:
            """raise an error"""
            raise ValueError("height must be >= 0")
        else:
            """initiate private field __height"""
            self.__height = value
