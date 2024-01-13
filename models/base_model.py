#!/usr/bin/python3
"""Parent class Module representation"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Parent BaseModel class"""

    def __init__(self, *args, **kwargs):
        """BaseModel intialization
        args: any tuple
        kwargs: any dictionary item"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None and kwargs != {}:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    f_date = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(val, f_date)
                elif key != "__class__":
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """print class name, id ,dictionary"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """method saves date and time updates"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """method to get all dictionary keys/values"""
        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__
        return mydict

    @classmethod
    def all(cls):
        """method to get all class instances"""
        return [obj for obj in models.storage.all().values()
                if type(obj) == cls]

    @classmethod
    def count(cls):
        """method to get instances count of class"""
        return len([obj for obj in models.storage.all().values()
                    if type(obj) == cls])

    @classmethod
    def show(cls, id):
        """method to get an instance by ID"""
        k = "{}.{}".format(cls.__name__, id)
        return models.storage.all().get(k)

    @classmethod
    def destroy(cls, id):
        """method for destroying instance by ID"""
        k = "{}.{}".format(cls.__name__, id)
        objec = models.storage.all().get(k)
        if objec is not None:
            del models.storage.all()[k]
            models.storage.save()

    @classmethod
    def update(cls, id, attr_name, attr_val):
        """method for updating instance by ID and attr name & value"""
        objec = cls.show(id)
        if objec is not None:
            setattr(objec, attr_name, attr_val)
            objec.save()

    @classmethod
    def update_with_dict(cls, id, attr_dict):
        """method for updating instance by ID and dict representn"""
        objec = cls.show(id)
        if objec is not None:
            for k, val in attr_dict.items():
                if k not in ["id", "created_at", "updated_at"]:
                    setattr(objec, k, val)
            objec.save()
