#!/usr/bin/python3
"""
Shebang used to make PYTHON script
"""


class MyInt(int):
    """class Myint whicj inherite int object"""
    def __init__(self, value):
        """method __init__"""
        super().__init__()

    def __eq__(self, other):
        """method equ, to invert"""
        return super().__ne__(other)

    def __ne__(self, other):
        """method not equal to invert to equal"""
        return super().__eq__(other)
