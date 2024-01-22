#!/usr/bin/python3
"""Unittest cases for Amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os
import pep8

class TestAmenity(unittest.TestCase):
    """"testing Class Amenity"""

    def setUp(self):
        """SetUp tests"""
        self.amenity = Amenity()
        self.amenity.name="swimming"
    def tearDown(self):
        """"Restart tests"""
        del self.amenity
        try:
            os.remove("jf")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test instantiation of the class"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test attributes of the class"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertEqual(self.amenity.name, "swimming")
        self.assertTrue('created_at' in self.amenity.__dict__)

    def test_attributeType(self):
        """check if attribute is string"""
        self.assertEqual(type(self.amenity.name), str)

    def test_to_dict(self):
        """Test to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("name", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_doc(self):
        """check class documentation"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_subClass(self):
        """check inheritance"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_style(self):
        """test pep8 style"""
        file_style = pep8.StyleGuide(quiet=True)
        style = style.check_files(['models/amenity.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
