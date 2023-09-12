#!/usr/bin/python3
"""
Shebang to create a python script
"""


import json


def from_json_string(my_str):
    """function to return python represantation of a JSON string"""
    return json.loads(my_str)
