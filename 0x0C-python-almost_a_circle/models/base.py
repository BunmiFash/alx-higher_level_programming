#!/usr/bin/python3

"""MODULE base which creates a class Base
"""

import json
import os
import csv


class Base:
    """Base class with private class sttributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing...
        if id is not None, assign the public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation"""
        if (
                list_dictionaries is None
                or len(list_dictionaries) < 1):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves string representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding='UTF8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                list_json = Base.to_json_string(list_dict)
                f.write(list_json)

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string representation"""
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(4, 3)
        elif cls.__name__ == 'Square':
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"
        list_dict = []
        list_instance = []

        if os.path.exists(file_name):
            with open(file_name, mode='r', encoding='UTF8') as a_file:
                a_file_out = a_file.read()
                list_dict = cls.from_json_string(a_file_out)
                for i in list_dict:
                    list_instance.append(cls.create(**i))
        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves instances to CSV"""
        file_name = cls.__name__ + '.csv'
        with open(file_name, "w", newline="", encoding='UTF8') as a_file:
            if list_objs is None or len(list_objs) < 1:
                a_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                write_to = csv.DictWriter(a_file, fieldnames=keys)

                for obj in list_objs:
                    write_to.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return instances from csv"""
        file_name = cls.__name__ + '.csv'
        try:
            with open(file_name, "r", newline="") as a_file:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(a_file, fieldnames=keys)
                list_dict = [
                        dict([key, int(val)] for key, val in obj.items())
                        for obj in list_dict]
                return [cls.create(**f) for f in list_dict]
        except IOError:
            return []
