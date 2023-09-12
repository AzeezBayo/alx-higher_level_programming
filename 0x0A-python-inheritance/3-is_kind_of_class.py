#!/usr/bin/python3
"""This creates a function thats returns true
 with prototype is_kind_of_class(obj)"""


def is_kind_of_class(obj, a_class):
    """
        Function to return True if an object is exactly an instance
        of a specified clase else False
    """

    return isinstance(obj, a_class)

