#!/usr/bin/python3
""" this module returns json of an object"""


def to_json_string(my_obj):
    """defines a function that returns the JSON rep of an obj"""
    import json

    json_rep = json.dumps(my_obj)
    return json_rep

