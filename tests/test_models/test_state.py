#!/usr/bin/python3
"""Unittest cases for State"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """"testing Class State"""

    def setUp(self):
        """new state"""
        self.state = State(name="Ghaza")

    def tearDown(self):
        """"delete state"""
        del self.state

    def test_instantiation(self):
        """ensure type class"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """class attributes"""
        self.assertEqual(self.state.name, "Ghaza")

    def test_to_dict(self):
        """to_dict method testing"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("name", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()

