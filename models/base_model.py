#!/usr/bin/python3
"""
    The base model file
"""


from datetime import datetime
import uuid
import models


class BaseModel:
    """
        The BaseModel class is created that will define all common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """
            Public instance attributes are initialized
        """
        if (kwargs):
            for key, value in enumerate(kwargs):
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%h:%M:%S.%f")
                if key != '__class__':
                    self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """
            Updated the updated_at attribute with new.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
            String representation of the object
        """

        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
    
    def to_dict(self):
        """
            gives a dict of object
        """

        dictionary = dict(self.__dict__)
        dictionary['__class__'] = str(self.__class__.__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
