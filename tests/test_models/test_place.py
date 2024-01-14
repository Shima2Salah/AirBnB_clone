#!/usr/bin/python3
"""Unittest cases for Place"""

import unittest
from models.place import Place
from models.base_model import BaseModel
import os
import pep8

class TestPlace(unittest.TestCase):
    """"testing Class Place"""

    def setUp(self):
        """SetUp tests"""
        self.place = Place()
        self.place.name="palastine hotel"
        self.place.description = "war every way"
        self.place.number_rooms=1
        self.place.number_bathrooms=1
        self.place.max_guest=2
        self.place.price_by_night=200
        self.place.latitude=56.5
        self.place.longitude=-76.5
        self.place.amenity_ids=["1"]
        self.place.city_id="1"
        self.place.user_id="1"

    def tearDown(self):
        """"Restart tests"""
        del self.place
        try:
            os.remove("jf")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test instantiation of the class"""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Test attributes of the class"""
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.user_id, "1")
        self.assertEqual(self.place.name, "palastine hotel")
        self.assertEqual(self.place.description, "war every way")
        self.assertEqual(self.place.number_rooms, 1)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 2)
        self.assertEqual(self.place.price_by_night, 200)
        self.assertEqual(self.place.latitude, 56.5)
        self.assertEqual(self.place.longitude, -76.5)
        self.assertEqual(self.place.amenity_ids, ["1"])

    def test_to_dict(self):
        """Test to_dict method"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertIn("name", place_dict)
        self.assertIn("description", place_dict)
        self.assertIn("number_rooms", place_dict)
        self.assertIn("number_bathrooms", place_dict)
        self.assertIn("max_guest", place_dict)
        self.assertIn("price_by_night", place_dict)
        self.assertIn("latitude", place_dict)
        self.assertIn("longitude", place_dict)
        self.assertIn("amenity_ids", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated_at)
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_doc(self):
        """check class documentation"""
        self.assertIsNotNone(Place.__doc__)

    def test_subClass(self):
        """check inheritance"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attributeType(self):
        """check if attribute is string"""
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)

    def test_style(self):
        """test pep8 style"""
        file_style = pep8.StyleGuide(quiet=True)
        style = style.check_files(['models/place.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
