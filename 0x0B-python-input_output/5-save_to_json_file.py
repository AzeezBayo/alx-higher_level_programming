#!/usr/bin/python3
"""this module uses json rep to write a file"""


def save_to_json_file(my_obj, filename):
    """write an object to a text file using json rep"""
    import json

    with open(filename, "w") as file:
        json.dump(my_obj, file)

