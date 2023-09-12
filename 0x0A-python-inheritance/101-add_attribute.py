#!/usr/bin/python3
"""module adds attributes to objects."""


def add_attribute(obj, att, value):
    """define a function that add a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

