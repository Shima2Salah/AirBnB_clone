#!/usr/bin/python3
"""Unittest cases for City"""

import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """"testing Class City"""

    def setUp(self):
        """SetUp tests"""
        self.city = City()
        self.city.state_id="ps"
        self.city.name="palastine"

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
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)

    def test_attributeType(self):
        """check if attribute is string"""
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city.name), str)

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
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_doc(self):
        """check class documentation"""
        self.assertIsNotNone(City.__doc__)

    def test_subClass(self):
        """check inheritance"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
