#!/usr/bin/python3
"""Unittest cases for State"""

import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """"testing Class State"""

    def setUp(self):
        """new state"""
        self.state = State()
        self.state.name = "Ghaza"

    def tearDown(self):
        """"delete state"""
        del self.state

    def test_instantiation(self):
        """ensure type class"""
        self.assertIsInstance(self.state, State)

    def test_subClass(self):
      """check if instance class is subclass"""
      self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attributes(self):
        """class attributes"""
        self.assertEqual(self.state.name, "Ghaza")
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        

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

    def test_doc(self):
      """check class documentation"""
      self.assertIsNotNone(State.__doc__)

if __name__ == "__main__":
    unittest.main()
