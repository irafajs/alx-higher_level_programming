#!/usr/bin/python3
"""
Shebang used to make python script
"""


def add_attribute(obj, attribute, value):
    """add a new attr to an object, raise an eror if obj cant have new att"""
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__')
            and attribute in type(obj).__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
