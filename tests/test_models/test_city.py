#!/usr/bin/python3
"""Unittest cases for City"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """"testing Class City"""

    def setUp(self):
        """SetUp tests"""
        self.city = City(state_id="ps", name="palastine")

    def tearDown(self):
        """"Restart tests"""
        del self.city

    def test_instantiation(self):
        """Test instantiation of the class"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test attributes of the class"""
        self.assertEqual(self.city.state_id, "ps")
        self.assertEqual(self.city.name, "palastine")

    def test_to_dict(self):
        """Test to_dict method"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()

