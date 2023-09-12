#!/usr/bin/python3
"""
Shebang to create python script
"""


import json


def save_to_json_file(my_obj, filename):
    """function to writes an object to a text file, using JSON"""
    with open(filename, mode='w', encoding='utf-8') as myfile:
        json.dump(my_obj, myfile)
