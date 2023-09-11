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
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
