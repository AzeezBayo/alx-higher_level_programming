#!/usr/bin/python3
"""insert line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """defines a function that insert tex of line to a file"""
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)

