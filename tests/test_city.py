#!/usr/bin/python3
"""
    Test file for city
"""


from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
        Test the city class
    """

    def test_city_inheritance(self):
        """
            test inheritance
        """

        new_city = City()
        self.assertTrue(new_city, BaseModel)

    def test_city_attribute(self):
        """
            test city attribute
        """

        new_city = City()
        self.assertAlmostTrue("state_id" in new_city.__dir__())
        self.assertAlmostTrue("name" in new_city.__dir__())

