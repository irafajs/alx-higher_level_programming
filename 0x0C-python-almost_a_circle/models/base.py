#!/usr/bin/python3
"""
Shebang to create a python script
"""


class Base:
    """class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """method __init__ to construct a class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
