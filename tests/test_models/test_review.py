#!/usr/bin/python3
"""Unittest cases for Review"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """"testing Class Review"""

    def setUp(self):
        """new Review"""
        self.review = Review(place_id="1", user_id="1", text="so good")

    def tearDown(self):
        """"delete review"""
        del self.review

    def test_instantiation(self):
        """ensure type class"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """class attributes"""
        self.assertEqual(self.review.place_id, "1")
        self.assertEqual(self.review.user_id, "1")
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

    def test_save(self):
        """Test save method"""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
