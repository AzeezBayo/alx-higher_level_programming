#!/usr/bin/python3
"""modue creats object"""


import json


def load_from_json_file(filename):
    """ defines a function that creates an object from a JSON file"""
    with open(filename, encoding="utf-8") as my_file:
        return json.load(my_file)

