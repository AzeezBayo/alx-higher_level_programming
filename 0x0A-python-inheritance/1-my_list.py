#!/usr/bin/python3
"""This creates a class with MyList(list)"""


class MyList(list):
    """defines a class MyList that inherits from list:"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))

