#!/usr/bin/python3
""" this module returns an object rep of json"""


def from_json_string(my_str):
    """defines a function that returns an obj rep of JSON"""
    import json

    json_rep = json.loads(my_str)
    return (json_rep)

