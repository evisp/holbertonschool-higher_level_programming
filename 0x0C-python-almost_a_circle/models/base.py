#!/usr/bin/python3
""" first class Base """
import json
from os import path


class Base:
    """ Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to JSON definition """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representatios to a file, definition """
        empty_list = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            empty_list = [x.to_dictionary() for x in list_objs]
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """ from JSON to string definition """
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ definition """
        dummy_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ definition """
        filename = cls.__name__ + ".json"
        if path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                dictionary = cls.from_json_string(file.read())
                list_of_instances = [cls.create(**inst) for inst in dictionary]
                return list_of_instances
        else:
            return []
