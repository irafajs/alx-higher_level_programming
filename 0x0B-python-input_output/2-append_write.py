#!/usr/bin/python3
"""
Shebang to create a python script
"""


def append_write(filename="", text=""):
    """function to append text to the file"""
    with open(filename, mode='a', encoding='utf-8') as myfile:
        return myfile.write(text)
