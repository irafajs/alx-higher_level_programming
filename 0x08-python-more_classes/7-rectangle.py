#!/usr/bin/python3
"""defines class named Rectangle"""


class Rectangle:
    """initialize attributes to 0"""
    number_of_instances = 0
    """initialize attribute to str #"""
    print_symbol = '#'
    """defines function named __init__"""
    def __init__(self, width=0, height=0):
        """initialize width to width"""
        self.width = width
        """initialize height to height"""
        self.height = height
        """increment instance at instantiation"""
        Rectangle.number_of_instances += 1
    """defines function named width as getter"""
    @property
    def width(self):
        """return private field __width"""
        return self.__width
    """defines function named width as setter"""
    @width.setter
    def width(self, value):
        """if statement block"""
        if not isinstance(value, int):
            """raise an error when if is false"""
            raise TypeError("width must be an integer")
        elif value < 0:
            """raise an error if value is lesser than 0"""
            raise ValueError("width must be >= 0")
        else:
            """initialize __width to value"""
            self.__width = value
    """defines a function named height as getter"""
    @property
    def height(self):
        """return private field height"""
        return self.__height
    """defines function height as setter"""
    @height.setter
    def height(self, value):
        """if statement block"""
        if not isinstance(value, int):
            """raise an error when if statement is false"""
            raise TypeError("height must be an integer")
        elif value < 0:
            """raise an error when value is less than 0"""
            raise ValueError("height must be >= 0")
        else:
            """initialize __height to value"""
            self.__height = value
    """defines a function named area"""
    def area(self):
        """return the area calculation"""
        return self.height * self.width
    """defines a function named perimeter"""
    def perimeter(self):
        """if statment block"""
        if self.width == 0 or self.height == 0:
            """return 0 once one of field is equal to 0"""
            return 0
        else:
            """return perimeter calculation"""
            return (2 * (self.height + self.width))
    """defines function __str__"""
    def __str__(self):
        """if statement block"""
        if self.__width == 0 or self.__height == 0:
            """return empty string"""
            return ""
        """return the area printed in form of symbol#"""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)
    """defines function __repr___"""
    def __repr__(self):
        """return representaion of Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    """defines function del as a destructor"""
    def __del__(self):
        """decrement number of instances at instantiation"""
        Rectangle.number_of_instances -= 1
        """print the end message after deletion of class"""
        print("Bye rectangle...")
