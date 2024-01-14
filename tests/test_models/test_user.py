#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """
    Methods:
    setUp(self)
    tearDown(self)
    test_objAttributes(self)
    test_uniqueid(self)
    test_save(self)
    """
    def setUp(self):
        """set instance for testing"""
        self.test = User()
        self.test2 = User()
        self.test.first_name = "nermine"
        self.test.last_name = "sss"
        self.test.email = "sha@gmail.com"
        self.test.password = "1234"

    def tearDown(self):
        """delete instance after testing"""
        del self.test
        del self.test2

    def test_attributeType(self):
        """check if attribute is string"""
        self.assertEqual(type(self.test.first_name), str)
        self.assertEqual(type(self.test.last_name), str)
        self.assertEqual(type(self.test.email), str)
        self.assertEqual(type(self.test.password), str)

    def test_uniqueid(self):
        """check unique id generation"""
        self.assertNotEqual(self.test.id, self.test2.id)

    def test_save(self):
        self.test.save()
        self.assertNotEqual(self.test.created_at, self.test.updated_at)

    def test_doc(self):
        """check class documentation"""
        self.assertIsNotNone(User.__doc__)

    def test_subClass(self):
        """check inheritance"""
        self.assertTrue(issubclass(self.test.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
