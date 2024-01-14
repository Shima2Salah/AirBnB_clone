#!/usr/bin/python3
"""testing FileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import pep8

class TestFileStorage(unittest.TestCase):
    """
    Methods:
        setUp(self)
        tearDown(self)
        test_all(self)
        test_new(self)
        test_save_reload(self)
    """
    def setUp(self):
        """set instance to test class"""
        self.test_1 = FileStorage()
        self.test_2 = BaseModel()
        self.test_1.new(self.test_2)
        self.test_1.user_id = "ner"
        self.test_1.place_id = "egypt"
        self.m = FileStorage()

    def tearDown(self):
        """remove instance and file used in testing"""
        del self.test_1
        del self.test_2
        del self.m
        try:
            os.remove("jf")
        except FileNotFoundError:
            pass

    def clean_up(self):
        """remove file used in testing"""
        file_path = self.test_1.get_file_path()
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_all(self):
        """check if method return dictionary"""
        self.clean_up()
        self.assertIsInstance(self.test_1.all(), dict)
        self.assertIs(self.test_1.all(), self.test_1.get_object())
        self.assertEqual(type(self.test_1.all()), dict)
        self.assertIsNotNone(self.test_1.all())

    def test_new(self):
        """check if dictionary is set with key [class name.id]"""
        self.clean_up()
        key = "{}.{}".format(self.test_2.__class__.__name__, self.test_2.id)
        self.assertIn(key, self.test_1.get_object())

    def test_save_reload(self):
        """test serialization"""
        self.clean_up()
        key = "{}.{}".format(self.test_2.__class__.__name__, self.test_2.id)
        self.assertFalse(os.path.exists(self.test_1.get_file_path()))
        self.test_1.save()
        self.assertEqual(os.path.exists(self.test_1.get_file_path()), True)
        self.test_1.reload()
        self.assertIn(key, self.test_1.get_object())
        reloaded_obj = self.test_1.get_object()[key]
        self.assertEqual(self.test_2.to_dict(), reloaded_obj.to_dict())
        try:
            os.remove("jj")
        except FileNotFoundError:
            pass
        with open("jj", "w") as f:
            f.write("{}")
        with open("jj", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_style(self):
        """test pep8 style"""
        file_style = pep8.StyleGuide(quiet=True)
        style = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")
