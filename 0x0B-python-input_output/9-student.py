#!/usr/bin/python3
"""module of Student class"""


class Student:
    """define the class students"""
    def __init__(self, first_name, last_name, age):
        """initializes class object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return an object in dic rep"""

        return self.__dict__

