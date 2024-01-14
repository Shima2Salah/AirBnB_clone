#!/usr/bin/python3
"""Unittest cases for Place"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
   """"testing Class Place"""

   def setUp(self):
       """SetUp tests"""
       self.place = Place(city_id="1", user_id="1", name="palastine hotel", description="war every way", number_rooms=1, number_bathrooms=1, max_guest=2, price_by_night=200, latitude=56.5, longitude=-76.5, amenity_ids=["1"])

   def tearDown(self):
       """"Restart tests"""
       del self.place

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

   def test_save(self):
       """Test save method"""
       old_updated_at = self.place.updated_at
       self.place.save()
       self.assertNotEqual(self.place.updated_at, old_updated_at)


if __name__ == "__main__":
   unittest.main()

