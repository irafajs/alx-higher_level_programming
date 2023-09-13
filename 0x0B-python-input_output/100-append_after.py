#!/usr/bin/python3
"""
Shebang to create python script
"""


def append_after(filename="", search_string="", new_string=""):
    """function to append a new string if a match of key word is available"""
    with open(filename, mode='r', encoding='utf-8') as r_file:
        lines = r_file.readlines()
        with open(filename, mode='w', encoding='utf-8') as a_file:
            for read in lines:
                a_file.write(read)
                if search_string in read:
                    a_file.write(new_string)
