#!/usr/bin/python3
"""This creates a function with prototype lookup(obj)"""


def lookup(obj):
    """
        Returns the list of available attributes
        and methods of an object
    """
    return dir(obj)

