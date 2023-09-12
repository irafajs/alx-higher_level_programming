#!/usr/bin/python3
"""
Shebang to create a python script
"""

import json


def to_json_string(my_obj):
    """function that return JSON represantation of a string"""
    return json.dumps(my_obj)
