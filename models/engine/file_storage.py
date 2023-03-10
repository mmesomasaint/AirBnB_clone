#!/usr/bin/python3
"""serializes instances to JSON file, deserializes JSON file to instances"""


import json
from models.base_model import BaseModel


class FileStorage:
    """file storage creation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
         """returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """adds new object to __objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """saves objects to json file"""
        jsonData = {}
        for key, value in self.__objects.items():
            jsonData[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(jsonData, f)

    def reload(self):
        """reloads"""
                                                                        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for key, obj in data.items():
                newObj = eval(obj['__class__'])(**obj)
                self.__objects[key] = newObj
        except FileNotFoundError:
                pass
