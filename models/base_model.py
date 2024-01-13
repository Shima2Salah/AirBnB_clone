#!/usr/bin/python3
"""Parent class Module representation"""
from datetime import datetime
from uuid import uuid4
from models import storage


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
            storage.new(self)

    def __str__(self):
        """print class name, id ,dictionary"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """method saves date and time updates"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """method to get all dictionary keys/values"""
        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__
        return mydict
