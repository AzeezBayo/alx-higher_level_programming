#!/usr/bin/python3

""" MyInt class """


class MyInt(int):
    """defines a class that inverts == !=. operators """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

