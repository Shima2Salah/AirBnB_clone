#!/usr/bin/python3
"""Unittest cases for Amenity"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
  """"testing Class Amenity"""

  def setUp(self):
      """SetUp tests"""
      self.amenity = Amenity(name="swimming")

  def tearDown(self):
      """"Restart tests"""
      del self.amenity

  def test_instantiation(self):
      """Test instantiation of the class"""
      self.assertIsInstance(self.amenity, Amenity)

  def test_attributes(self):
      """Test attributes of the class"""
      self.assertEqual(self.amenity.name, "swimming")

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


if __name__ == "__main__":
  unittest.main()

