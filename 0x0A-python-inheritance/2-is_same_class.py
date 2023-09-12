#!/usr/bin/python3
"""This creates a function that returns true or false"""


def is_same_class(obj, a_class):
    """function returns True if the object is
    exactly an instance of the specified class otherwise False"""

    if type(obj) is a_class:
        return True
    else:
        return False

