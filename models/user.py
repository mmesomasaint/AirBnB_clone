#!/usr/bin/python3
"""
User class file
"""



from models.base_model import BaseModel


class User(BaseModel):
    """
    Class created
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
