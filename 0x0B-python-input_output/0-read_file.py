#!/usr/bin/python3
"""
Shebang to create a python script
"""


def read_file(filename=""):
    """function to read file content"""
    with open(filename, encoding='utf-8') as my_f:
        print("{}".format(my_f.read()), end="")
