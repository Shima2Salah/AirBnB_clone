#!/usr/bin/python3
"""Store elements to a file"""
import json
import os


class FileStorage:
    """Class that manage storage"""

    __file_path = 'file.json'
    __objects = {}

    def __init__(self, file__path=None):
        """"initialization for class"""
        if file__path is not None:
            FileStorage.__file_path = file__path

    def all(self):
        """"to get all class objects"""
        return FileStorage.__objects

    def new(self, obj):
        """"to add new class object"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """"serializes and to save objects to json file"""
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as jsfil:
            dict_fil = {}
            for k, v in FileStorage.__objects.items():
                dict_fil[k] = v.to_dict()
            json.dump(dict_fil, jsfil)

    def reload(self):
        """"deserializes and to reload objects from json file"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: globals()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
