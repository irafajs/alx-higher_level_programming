#!/usr/bin/python3
"""
Shebang to create a python script
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherit object of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """function init to initilize attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """function width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """function width setter"""
        self.__width = value

    @property
    def height(self):
        """funciton height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """function height setter"""
        self.__height = value

    @property
    def x(self):
        """function x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """function x setter"""
        self.__x = value

    @property
    def y(self):
        """function y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """function y setter"""
        self.__y = value
