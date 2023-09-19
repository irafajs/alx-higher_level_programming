#!/usr/bin/python3
"""
Shebang to create a python script
"""


import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instance"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as r_file:
                json_data = r_file.read()
                obj_dicts = cls.from_json_string(json_data)
                instances = [cls.create(**obj_dict) for obj_dict in obj_dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write to a file format .csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as w_file:
            writer = csv.writer(w_file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """read from a .csv file format"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as r_file:
                reader = csv.reader(r_file)
                instances = []
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        obj_dict = {
                                'id': int(row[0]),
                                'width': int(row[1]),
                                'height': int(row[2]),
                                'x': int(row[3]),
                                'y': int(row[4])
                                }
                    elif cls.__name__ == 'Square':
                        obj_dict = {
                                'id': int(row[0]),
                                'size': int(row[1]),
                                'x': int(row[2]),
                                'y': int(row[3])
                                }
                    instances.append(cls.create(**obj_dict))
                return instances
        except FileNotFoundError:
            return []
