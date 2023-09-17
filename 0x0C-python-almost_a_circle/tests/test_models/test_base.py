#!/usr/bin/python3
"""Tests case for base.py"""

import json
from models.base import Base
from models.rectangle import Rectangle
import unittest

class TestBase(unittest.TestCase):
    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_with_id(self):
        Base._Base__nb_objects = 0
        obj = Base(75)
        self.assertEqual(obj.id, 75)

    def test_with_string_id(self):
        base_instance = Base("Hello")
        self.assertEqual(base_instance.id, "Hello")
        base_instance = Base("Heyy")
        self.assertEqual(base_instance.id, "Heyy")

    def test_with_no_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_type(self):
        self.assertEqual(type(Base), type)
    
    def test_id_public(self):
        b = Base(25)
        b.id = 35
        self.assertEqual(35, b.id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_empty_to_json_string(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_to_json_string(self):
        r_inst = Rectangle(10, 17, 2, 8, 70)
        json_data = Base.to_json_string([r_inst.to_dictionary()])
        self.assertEqual(type(json_data), str)

    def test_to_json_string(self):
        rect_data = {'id': 31, 'x': 14, 'y': 10, 'width': 5, 'height': 5}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '[{"id": 31, "x": 14, "y": 10, "width": 5, "height": 5}]'
        )

    def test_save_to_file(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(8, 7, 0, 0, 12)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_create(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(str(r2), '[Rectangle] (12) 2/1 - 4/6')
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_from_json_string(self):
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    
    def test_load_from_file(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(4, 6)
        Rectangle.save_to_file([r1, r2])
        lst = Rectangle.load_from_file()
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), 2)
        self.assertIsInstance(lst[0], Rectangle)
        self.assertEqual(lst[0].__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertIsInstance(lst[1], Rectangle)
        self.assertEqual(lst[1].__str__(), "[Rectangle] (1) 0/0 - 4/6")



if __name__ == "__main__":
    unittest.main()


