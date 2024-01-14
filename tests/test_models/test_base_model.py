#!/usr/bin/python3
"""testing base_model class"""


import unittest
from models.base_model import BaseModel
from uuid import uuid4
import os
import pep8
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """
    Methods:
        setUp(self)
        tearDown(self)
        test_id(self)
        test_unique(self)
        test_date(self)
        test_update(self)
        test_kwargs(self)
        test_to_dict(self)
    """
    def setUp(self):
        """create BaseModel instance that will be used in test cases"""
        self.instance_1 = BaseModel()
        self.instance_2 = BaseModel()
        self.instance_1.name = "ner"
        self.instance_1.my_number = 7

    def tearDown(self):
        """remove instance created for testing"""
        del self.instance_1
        del self.instance_2
        try:
            os.remove("js")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """check attributes in class"""
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "__init__"))

    def test_id(self):
        """
        checking if id is generated from uuid testing id
        and then converted to string
        """
        self.assertIsInstance(self.instance_1.id, str)

    def test_inst(self):
        """check if object is class instance"""
        self.assertTrue(isinstance(self.instance_1, BaseModel))

    def test_unique(self):
        """test the generation of unique ids"""
        self.assertNotEqual(self.instance_1.id, self.instance_2.id)

    def test_date(self):
        """test type of date"""
        self.assertIsInstance(self.instance_1.created_at, datetime)
        self.assertIsInstance(self.instance_1.updated_at, datetime)

    def test_save(self):
        """check the change in time when update and save"""
        before_save = self.instance_1.updated_at
        self.instance_1.save()
        after_save = self.instance_1.updated_at
        self.assertNotEqual(before_save, after_save)
        self.instance_2.save()
        self.assertNotEqual(self.instance_2.created_at,
                            self.instance_2.updated_at)

    def test_kwargs(self):
        """test unpacking arg"""
        create_date = "2024-01-04T10:00:00.000000"
        update_date = "2024-02-03T10:00:00.000000"
        kwargs_output = {
                "id": str(uuid4()),
                "created_at": create_date,
                "updated_at": update_date
                }
        kwargs_inst = BaseModel(**kwargs_output)
        self.assertEqual(kwargs_inst.id, kwargs_output["id"])
        f = ".000000"
        self.assertEqual(kwargs_inst.created_at.isoformat() + f, create_date)
        self.assertEqual(kwargs_inst.updated_at.isoformat() + f, update_date)
        self.assertIsInstance(kwargs_inst.updated_at, datetime)
        self.assertIsInstance(kwargs_inst.created_at, datetime)

    def test_doc(self):
        """check for documenting"""
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)

    def test_to_dict(self):
        dictionary = self.instance_1.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(self.instance_1.__class__.__name__, 'BaseModel')
        self.assertEqual(dictionary["__class__"], "BaseModel")
        self.assertEqual(dictionary["id"], str(self.instance_1.id))
        self.assertIsInstance(dictionary["created_at"], str)
        self.assertIsInstance(dictionary["updated_at"], str)

    def test_style(self):
        """test pep8 style"""
        file_style = pep8.StyleGuide(quiet=True)
        style = style.check_files(['models/base_model.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def setUptwo(self):
        """Set up function for the tests."""
        self.first_m = BaseModel()
        self.second_m = BaseModel()

    def test_idtwo(self):
        """Test that the id is a string."""
        self.assertIsInstance(self.first_m.id, str)
        self.assertNotEqual(self.first_m.id, self.second_m.id)

    def test_created_attwo(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(self.first_m.created_at, datetime)
        self.assertNotEqual(self.first_m.created_at, self.second_m.created_at)

    def test_updated_attwo(self):
        """Test that updated_at is a datetime object."""
        self.assertIsInstance(self.first_m.updated_at, datetime)
        self.assertNotEqual(self.first_m.updated_at, self.second_m.updated_at)

    def test_savetwo(self):
        """Test that the save method updates updated_at."""
        old_time = self.first_m.updated_at
        self.first_m.save()
        self.assertGreater(self.first_m.updated_at, old_time)

    def test_to_dicttwo(self):
        """Test that to_dict returns a dictionary."""
        self.assertIsInstance(self.first_m.to_dict(), dict)

    def test_to_dict_contentstwo(self):
        """Test that to_dict includes the right keys."""
        m_dict = self.first_m.to_dict()
        self.assertIn('id', m_dict)
        self.assertIn('created_at', m_dict)
        self.assertIn('updated_at', m_dict)
        self.assertIn('__class__', m_dict)

    if __name__ == "__main__":
        unittest.main()
