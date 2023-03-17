#!/usr/bin/python3
"""
    Unittest file
"""


from models.base_model import BaseModel
from models.state import State
import unittest



class TestState(unittest.TestCase):
    """
        Test the State class
    """

    def test_state_inheritance(self):
        """
            Test the state class inherited from BaseModel
        """
        
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_state_attributes(self):
        """
            State class contain attribute name
        """

        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_state_attributes_type(self):
        """
            run a test to check state class contain a string attribute
        """

        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
