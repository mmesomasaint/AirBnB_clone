#!/usr/bin/python3
"""serializes instances to JSON file, deserializes JSON file to instances"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import models


class FileStorage:
    """file storage creation"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
         """returns the dictionary of objects"""

         return FileStorage.__objects

    def new(self, obj):
        """adds new object to __objects"""
        if obj:
            objname = obj.__class__.__name__
            key = "{}.{}".format(objname, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """saves objects to json file"""
        jsonData = {}
        for key, value in FileStorage.__objects.items():
            jsonData[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(jsonData, f)

    def reload(self):
        """reloads"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
            for key, obj in data.items():
                newObj = eval(obj['__class__'])(**obj)
                self.__objects[key] = newObj
        except FileNotFoundError:
                pass
