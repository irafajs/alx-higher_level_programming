#!/usr/bin/python3
"""
This is Shebang used to make PY cripting
"""


class BaseGeometry:
    """class named BaseGeometry"""
    def area(self):
        """method that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validator int"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class rectangle inherite object of BaseGeometry"""
    def __init__(self, width, height):
        """method to initiate private fields"""
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def area(self):
        """method area to calculate area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """magic method to print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """class square to calculate square of rectanlge"""
    def __init__(self, size):
        """method to make the square calc work"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """magic method to print square info"""
        return "[Square] {}/{}".format(self.__size, self.__size)
