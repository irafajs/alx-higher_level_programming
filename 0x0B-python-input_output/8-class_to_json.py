#!/usr/bin/python3
"""
Shebang to create python script
"""


def class_to_json(obj):
    """Serialize an object to a dictionary."""
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            json_dict[key] = value
    return json_dict
