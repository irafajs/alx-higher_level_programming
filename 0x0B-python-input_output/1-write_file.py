#!/usr/bin/python3
"""
Shebang to create python sript
"""


def write_file(filename="", text=""):
    """function to write to a file"""
    with open(filename, mode='w', encoding='utf-8') as myfile:
        myfile.write(text)
        return myfile.tell()
