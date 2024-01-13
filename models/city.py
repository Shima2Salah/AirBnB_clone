#!/usr/bin/python3
"""class for all users data"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""
