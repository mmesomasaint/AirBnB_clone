#!/usr/bin/python3
"""
    The base model file
"""


from datetime import datetime
import models
import uuid


class BaseModel:
    """
        The BaseModel class is created that will define all common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """
            Public instance attributes are initialized
        """
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """
            String representation of the object
        """

        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """
            update the public instance attribute with the current datetime
        """

        models.storage.save()
        self.updated_at = datetime.today()

    def to_dict(self):
        """
            Return the dictionary representation of an object
        """

        dictionary = dict(self.__dict__)
        dictionary['__class__'] = str(self.__class__.__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
