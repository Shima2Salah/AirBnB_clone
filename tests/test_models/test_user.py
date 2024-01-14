#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
import os
import pep8


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
        try:
            os.remove("jf")
        except FileNotFoundError:
            pass

    def test_objAttributes(self):
        """check attributes"""
        self.assertTrue(hasattr(self.test.__dict__, 'id'))
        self.assertTrue(hasattr(self.test.__dict__, 'created_at'))
        self.assertTrue(hasattr(self.test.__dict__, 'updated_at'))
        self.assertTrue(hasattr(self.test.__dict__, 'email'))
        self.assertTrue(hasattr(self.test.__dict__, 'password'))
        self.assertTrue(hasattr(self.test.__dict__, 'first_name'))
        self.assertTrue(hasattr(self.test.__dict__, 'last_name'))

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

    def test_style(self):
        """test pep8 style"""
        file_style = pep8.StyleGuide(quiet=True)
        style = style.check_files(['models/user.py'])     
        self.assertEqual(style.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
