#!/usr/bin/python3
"""Module of student class"""


class Student:
    """define the class students"""

    def __init__(self, first_name, last_name, age):
        """initializes class object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dict rep of student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            setattr(self, key, json[key])

