#!/usr/bin/python3
"""Test cases for square.py"""
import io
from models.square import Square
from models.base import Base
import unittest


class TestSquare(unittest.TestCase):

    def test_init(self):
        Base._Base__nb_objects = 0
        s = Square(10)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_init_with_given_attr(self):
        s = Square(10, 4, 6, 2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)

    def test_size_property(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_string_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10.27)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, None)

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "hello")

    def test_invalid_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -4)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 4.27)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 4, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 4, "hello")

    def test_invalid_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 4, -1)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 4, 6.27)

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            Square(8, 10, 4, 8, 2, 1)

    def test_less_args(self):
        with self.assertRaises(TypeError):
            Square(8)
            Square()
            Square(None)

    def test_class(self):
        s = Square(10)
        self.assertEqual(type(s), Square)

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(5, 0, 0).area(), 25)

    def test_update(self):
        s = Square(5)
        s.update(2)
        self.assertEqual(s.id, 2)
        s.update(2, 8)
        self.assertEqual(s.size, 8)
        s.update(2, 8, 4)
        self.assertEqual(s.x, 4)
        s.update(2, 8, 4, 6)
        self.assertEqual(s.y, 6)
        s.update(id=3)
        self.assertEqual(s.id, 3)
        s.update(size=10)
        self.assertEqual(s.size, 10)
        s.update(x=3, y=5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_update_kwargs(self):
        s = Square(10, 4, 6, 2)
        with self.assertRaises(TypeError):
            s.update(size="hello")
        with self.assertRaises(TypeError):
            s.update(x="hello")
        with self.assertRaises(TypeError):
            s.update(y="hello")
        with self.assertRaises(ValueError):
            s.update(size=-8)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-4)
        with self.assertRaises(ValueError):
            s.update(y=-6)

    def test_to_dictionary(self):
        s = Square(10, 4, 6, 2)
        expected_dict = {'id': 2, 'size': 10, 'x': 4, 'y': 6}
        self.assertDictEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()

