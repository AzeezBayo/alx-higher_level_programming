#!/usr/bin/python3
"""function writes to a text file returns no of char writen"""


def write_file(filename="", text=""):
    """ writes and return number of text written"""
    with open(filename,  'w') as file:
        word = file.write(text)
        return word

