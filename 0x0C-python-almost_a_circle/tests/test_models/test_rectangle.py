#!/usr/bin/python3
"""Tests case for rectangle.py"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        r = Rectangle(8, 10, 4, 6, 2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 6)
        self.assertEqual(r.id, 2)

    def test_rectangle_default_attr(self):
        r = Rectangle(8, 10)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)


class TestRectangleWidth(unittest.TestCase):

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 10)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 10)

    def test_invalid_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 10)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(8.27, 10)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(8, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(8, "hello")

    def test_invalid_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(8, 0)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(8, 10.27)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(8, 10, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(8, 10, "hello")

    def test_invalid_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(8, 10, -1)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(8, 10, 4.27)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(8, 10, 4, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(8, 10, 4, "hello")

    def test_invalid_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(8, 10, 4, -1)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(8, 10, 4, 6.27)

    def test_area_calculation(self):
        r = Rectangle(8, 10)
        self.assertEqual(r.area(), 80)

    def test_area_calculation_with_coordinates(self):
        r = Rectangle(8, 10, 0, 0, 2)
        self.assertEqual(r.area(), 80)

    def test_area_small(self):
        r = Rectangle(8, 10, 0, 0, 0)
        self.assertEqual(r.area(), 80)

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(8, 10, 4, 8, 2, 1)

    def test_less_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(8)
            r = Rectangle()
            r = Rectangle(None)

    def test_update_with_args(self):
        r = Rectangle(8, 10, 4, 6, 2)
        r.update(1, 7, 9, 3, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 5)

    def test_update_with_kwargs(self):
        r = Rectangle(8, 10, 4, 6, 2)
        r.update(id=2, width=7, height=9, x=3, y=5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 5)


if __name__ == "__main__":
    unittest.main()


