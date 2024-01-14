#!/usr/bin/python3
"""Unittest cases for Review"""

import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """"testing Class Review"""

    def setUp(self):
        """new Review"""
        self.review = Review()
        self.review.place_id = "1"
        self.review.user_id = "123"
        self.review.text = "so good"

    def tearDown(self):
        """"delete review"""
        del self.review

    def test_instantiation(self):
        """ensure type class"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """class attributes"""
        self.assertEqual(self.review.place_id, "1")
        self.assertEqual(self.review.user_id, "123")
        self.assertEqual(self.review.text, "so good")

    def test_to_dict(self):
        """to_dict method testing"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("__class__", review_dict)
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_subClass(self):
        """check inheritance"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_doc(self):
        """check class documentation"""
        self.assertIsNotNone(Review.__doc__)
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_attributeType(self):
        """check if attribute is string"""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

if __name__ == "__main__":
    unittest.main()
