#!/usr/bin/python3
"""creates a function Rectangle"""

import json
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""


    def __init__(self, size, x=0, y=0, id=None):
        """takes in similar arguments to rectangle"/
        "replaces width and height with size"""
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
            string representation of Square class instance
        """
        return "[{}] ({}) {}/{} - {}" \
            .format(self.__class__.__name__, self.id,
                    self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """updates propeties of a class instance"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return the dict rep of a Rectangle."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

