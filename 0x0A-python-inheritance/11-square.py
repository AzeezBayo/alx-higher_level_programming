#!/usr/bin/python3
"""This module creates a class for task 9"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle extends from  BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)


class Square(Rectangle):
    """Define a square(rectangle) """
    def __init__(self, size):
        """initialze the square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns area of the square"""
        return self.__size ** 2

