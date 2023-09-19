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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """funciton height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """function height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """function x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """function x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """function y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """function y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """method named area"""
        return self.__height * self.__width

    def display(self):
        """method named display"""
        for y_ele in range(self.__y):
            print()
        for item in range(self.__height):
            for x_element in range(self.__x):
                print(" ", end="")
            for element in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """method __str__"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """method update to assigne argument"""
        arg_names = ("id", "width", "height", "x", "y")
        if args:
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method to_dictionary that returns a dict representaion"""
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                }

    @classmethod
    def create(cls, **kwargs):
        """create a metjod to create new rectangle with create keyword"""
        new_rect = cls(1, 1)
        new_rect.update(**kwargs)
        return new_rect
