#!/usr/bin/python3
"""
Shebang to create a python script
"""


import json


class Base:
    """class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """method __init__ to construct a class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method to_json_string to return JSON repr of list_dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method to save json string to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as w_file:
            json_str = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
            )
            w_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """method to convert json string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance with attributtes"""
        inst_dum = cls.__new__(cls)
        inst_dum.__dict__.update({'width': 1, 'height': 1, 'x': 0, 'y': 0})
        inst_dum.update(**dictionary)
        return inst_dum
