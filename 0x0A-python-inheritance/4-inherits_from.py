#!/usr/bin/python3
"""
This is a Shebang used to make python script
"""


def inherits_from(obj, a_class):
    """true if obj is instance of a_class else false"""
    return isinstance(obj, a_class) and obj.__class__ != a_class
