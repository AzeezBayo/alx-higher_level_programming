#!/usr/bin/python3
"""the "class_to_json" function"""


def class_to_json(obj):
    """returns the dict for JSON serialization of an object"""
    return obj.__dict__

