#!/usr/bin/python3
"""append string to the end of a file"""


def append_write(filename="", text=""):
    """function add text to the end of filename and return no of char added"""
    with open(filename, 'a') as file:
        file.write(text)
        return(len(text))

