#!/usr/bin/python3
"""
Shebang to create python script
"""


import json


def load_from_json_file(filename):
    """function to crate object from JSON file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
