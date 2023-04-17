#!/usr/bin/python3

"""Module to test for the class Base"""

import unittest
from models.base import Base
import json
from models.rectangle import Rectangle
from models.square import Square


class TestBaseModule(unittest.TestCase):
    """TEST CASES FOR BASE CLASS"""
    def test_base_id_given(self):
        """id provided"""
        self.rect1 = Base(22)
        self.assertEqual(self.rect1.id, 22)

    def test_base_no_id(self):
        """NO ID PROVIDED"""
        self.rect2 = Base()
        self.rect3 = Base()

        self.assertEqual(self.rect2.id, 2)
        self.assertEqual(self.rect3.id, 3)

    def test_base_id_str(self):
        """STRING AS ID"""
        self.rect4 = Base("20")
        self.assertEqual(self.rect4.id, "20")

    def test_base_id_again(self):
        """PUBLIC ID CASE"""
        self.rect6 = Base(20)
        self.rect6.id = 23
        self.rect8 = Base()

        self.assertEqual(self.rect6.id, 23)
        self.assertEqual(self.rect8.id, 1)

    def test_base_with_float(self):
        """ID AS FLOAT"""
        self.rect10 = Base(9.8)
        self.assertEqual(self.rect10.id, 9.8)

    def test_base_with_more_than_one_arg(self):
        """MORE THAN ONE ARGUMENT PASSED AS ID"""
        self.assertRaises(TypeError, Base(), (9, 7))

    """
    TEST CASES FOR LIST_DICT TO JSON STRING - RECTANGLE
    """
    def test_base_empty_list_dict_to_json_string(self):
        """returns [] for empty list"""
        self.list1 = []
        self.json_list1 = Base.to_json_string(self.list1)
        self.assertEqual(self.json_list1, "[]")

    def test_base_none_list_dict_to_json_string(self):
        """returns [] for if list does not exist"""
        self.list2 = None
        self.json_list2 = Base.to_json_string(self.list2)
        self.assertEqual(self.json_list2, "[]")

    def test_base_list_dict_to_json_string(self):
        """returns the JSON string representation"""
        self.list3 = [{'one': 1, 'two': 2}]
        self.json_list3 = Base.to_json_string(self.list3)
        self.assertEqual(self.json_list3, '[{"one": 1, "two": 2}]')

    def test_base_list_two_dict_to_json_string(self):
        """returns the JSON string representation"""
        self.list4 = [
                {'on': 1, '2': 2},
                {'x': 'h', 'y': 'x', 'z': 't'}]
        self.json_list4 = Base.to_json_string(self.list4)
        self.res = '[{"on": 1, "2": 2}, {"x": "h", "y": "x", "z": "t"}]'
        self.assertEqual(self.json_list4, self.res)

    def test_base_rect_to_json(self):
        """Returns the JSON rep of Rectangle attributes"""
        self.rect1 = Rectangle(5, 3, 2, 3, 10)
        self.rect1_dict1 = self.rect1.to_dictionary()
        self.rect1_json = Base.to_json_string([self.rect1_dict1])
        self.assertEqual(
                self.rect1_json,
                '[{"x": 2, "y": 3, "id": 10, "height": 3, "width": 5}]')

    def test_base_two_rect_to_json(self):
        """Returns the JSON rep of Rectangle attributes"""
        self.rect2 = Rectangle(5, 3, 2, 3, 10)
        self.rect3 = Rectangle(2, 4, 6, 8, 9)
        self.rect2_dict2 = self.rect2.to_dictionary()
        self.rect3_dict3 = self.rect3.to_dictionary()
        self.rect_list = [self.rect2_dict2, self.rect3_dict3]
        self.rect_json = Base.to_json_string(self.rect_list)
        self.assertEqual(
                self.rect_json,
                '[{"x": 2, "y": 3, "id": 10, "height": 3, "width": 5},\
 {"x": 6, "y": 8, "id": 9, "height": 4, "width": 2}]'
                )

    def test_base_rect_to_dict_type(self):
        """Checks for the reteurn type of to_json_string"""
        self.rect4 = Rectangle(2, 4, 6, 8, 9)
        self.rect4_dict = self.rect4.to_dictionary()
        self.rect4_type = type(Base.to_json_string(self.rect4_dict))
        self.assertTrue(self.rect4_type, str)

    """
    TEST CASES FOR LIST_DICT TO JSON STRING - SQUARE
    """
    def test_base_one_sqr_to_json(self):
        """Converts attributes to json"""
        self.sqr1 = Square(4, 3, 2, 7)
        self.sqr1_dict = self.sqr1.to_dictionary()
        self.sqr1_json = Base.to_json_string([self.sqr1_dict])
        self.assertEqual(
                self.sqr1_json,
                '[{"id": 7, "x": 3, "size": 4, "y": 2}]')

    def test_base_two_sqr_to_json(self):
        """Converts attributes to json"""
        self.sqr2 = Square(4, 3, 2, 7)
        self.sqr3 = Square(5, 2, 1, 6)
        self.sqr2_dict = self.sqr2.to_dictionary()
        self.sqr3_dict = self.sqr3.to_dictionary()
        self.sqr_list = [self.sqr2_dict, self.sqr3_dict]
        self.sqr_json = Base.to_json_string(self.sqr_list)
        self.assertEqual(
                self.sqr_json,
                '[{"id": 7, "x": 3, "size": 4, "y": 2},\
 {"id": 6, "x": 2, "size": 5, "y": 1}]')

    def test_base_sqr_to_json_type(self):
        """Checks output type"""
        self.sqr4 = Square(5, 2, 1, 6)
        self.sqr4_dict = self.sqr4.to_dictionary()
        self.sqr4_type = Base.to_json_string([self.sqr4_dict])
        self.assertTrue(type(self.sqr4_type) == str)

    """
    TEST CASES FOR SAVING JSON STRING REPRESANTATION TO FILE - RECT
    """
    def test_save_to_file_none(self):
        """Test case to save json to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as file:
            self.assertTrue(file.read() == "[]")

    def test_save_to_file_empty_list(self):
        """Test case to save json to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as file:
            self.assertTrue(file.read() == "[]")

    def test_save_to_file_one_rect(self):
        """Test case to save json to file"""
        self.rect5 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([self.rect5])

        with open("Rectangle.json", 'r') as a_file:
            self.new = a_file.read()
            self.assertEqual(
                    self.new,
                    '[{"x": 4, "y": 5, "id": 6, "height": 3, "width": 2}]')

    def test_save_to_file_two_rect(self):
        """Test case to save json to file"""
        self.rect6 = Rectangle(2, 3, 4, 5, 6)
        self.rect7 = Rectangle(2, 4, 6, 8, 9)
        Rectangle.save_to_file([self.rect6, self.rect7])

        with open("Rectangle.json", 'r') as b_file:
            self.rectObj = b_file.read()
            self.assertEqual(
                    self.rectObj,
                    '[{"x": 4, "y": 5, "id": 6, "height": 3, "width": 2},\
 {"x": 6, "y": 8, "id": 9,\
 "height": 4, "width": 2}]')

    def test_save_to_file_over_write(self):
        """Test case to save json to file"""
        self.rect8 = Rectangle(2, 4, 6, 8, 9)
        Rectangle.save_to_file([self.rect8])

        self.rect9 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([self.rect9])

        with open("Rectangle.json", 'r') as c_file:
            self.newRect = c_file.read()
            self.assertEqual(
                    self.newRect,
                    '[{"x": 4, "y": 5, "id": 6, "height": 3, "width": 2}]')

    def test_save_to_file_no_arg(self):
        """Test case to save json to file"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    """
    TEST CASES FOR SAVING JSON STRING REPRESANTATION TO FILE - SQR
    """
    def test_save_to_file_sqr_none(self):
        """Test case to save json to file"""
        Square.save_to_file(None)
        with open("Square.json", 'r') as file:
            self.assertTrue(file.read() == "[]")

    def test_save_to_file_sqr_empty_list(self):
        """Test case to save json to file"""
        Square.save_to_file([])
        with open("Square.json", 'r') as file:
            self.assertTrue(file.read() == "[]")

    def test_save_to_file_one_square(self):
        """Test case to save json to file"""
        self.sqr5 = Square(2, 3, 4, 5)
        Square.save_to_file([self.sqr5])

        with open("Square.json", 'r') as a_file:
            self.new = a_file.read()
            self.assertEqual(
                    self.new,
                    '[{"id": 5, "x": 3, "size": 2, "y": 4}]')

    def test_save_to_file_two_sqr(self):
        """Test case to save json to file"""
        self.sqr6 = Square(2, 3, 4, 5)
        self.sqr7 = Square(2, 4, 6, 8)
        Square.save_to_file([self.sqr6, self.sqr7])

        with open("Square.json", 'r') as b_file:
            self.sqrObj = b_file.read()
            self.assertEqual(
                    self.sqrObj,
                    '[{"id": 5, "x": 3, "size": 2, "y": 4},\
 {"id": 8, "x": 4, "size": 2, "y": 6}]')

    def test_save_to_file_sqr_over_write(self):
        """Test case to save json to file"""
        self.sqr8 = Square(2, 4, 6, 8)
        Square.save_to_file([self.sqr8])

        self.sqr9 = Square(2, 3, 4, 5)
        Square.save_to_file([self.sqr9])

        with open("Square.json", 'r') as c_file:
            self.newSqr = c_file.read()
            self.assertEqual(
                    self.newSqr,
                    '[{"id": 5, "x": 3, "size": 2, "y": 4}]')

    def test_save_to_file_excess_arg(self):
        """Test case to save json to file"""
        with self.assertRaises(TypeError):
            Square.save_to_file()

    """TEST CASES FOR LOADS - RECTANGLE"""
    def test_from_json_string_none(self):
        """Test case for load from file"""
        self.resLoad = Rectangle.from_json_string(None)
        self.assertEqual(self.resLoad, [])

    def test_from_json_string_empty(self):
        """Test case for load from file"""
        self.resLoad1 = Rectangle.from_json_string([])
        self.assertEqual(self.resLoad1, [])

    def test_from_json_string_one_rect(self):
        """Test case for load from file"""
        self.rect10 = Rectangle(4, 5, 6, 7, 8)
        self.rect10 = self.rect10.to_dictionary()
        self.rectStr = Rectangle.to_json_string([self.rect10])
        self.rectObj = Rectangle.from_json_string(self.rectStr)

        self.assertEqual(
                self.rectObj,
                [{'x': 6, 'y': 7, 'id': 8, 'height': 5, 'width': 4}])

    def test_from_json_string_two_rect(self):
        """Test case for load from file"""
        self.rect11 = Rectangle(4, 5, 6, 7, 8)
        self.rect11 = self.rect11.to_dictionary()
        self.rect12 = Rectangle(1, 2, 3, 4, 5)
        self.rect12 = self.rect12.to_dictionary()
        self.rectStr = Rectangle.to_json_string([self.rect11, self.rect12])
        self.rectObj = Rectangle.from_json_string(self.rectStr)

        self.assertEqual(
                self.rectObj,
                [{'x': 6, 'y': 7, 'id': 8, 'height': 5, 'width': 4},
                    {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}])

    def test_from_json_string_type(self):
        """Checks the type of object returned"""
        self.rect13 = Rectangle(4, 5, 6, 7, 8)
        self.rect13 = self.rect13.to_dictionary()
        self.rectStr = Rectangle.to_json_string([self.rect13])
        self.rectObj = Rectangle.from_json_string(self.rectStr)

        self.assertTrue(type(self.rectObj) == list)

    def test_from_json_string_no_arg(self):
        """Checks for errors when no arg is given"""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

    """TEST CASES FOR LOADS - SQUARE"""
    def test_from_json_string_sqr_none(self):
        """Test case for load from file"""
        self.resLoad1 = Square.from_json_string(None)
        self.assertEqual(self.resLoad1, [])

    def test_from_json_string_sqr_empty(self):
        """Test case for load from file"""
        self.resLoad2 = Square.from_json_string([])
        self.assertEqual(self.resLoad2, [])

    def test_from_json_string_one_sqr(self):
        """Test case for load from file"""
        self.sqr10 = Square(4, 5, 6, 7)
        self.sqr10 = self.sqr10.to_dictionary()
        self.sqrStr = Square.to_json_string([self.sqr10])
        self.sqrObj = Square.from_json_string(self.sqrStr)

        self.assertEqual(
                self.sqrObj,
                [{'x': 5, 'id': 7, 'size': 4, 'y': 6}])

    def test_from_json_string_two_sqr(self):
        """Test case for load from file"""
        self.sqr11 = Square(4, 5, 6, 7)
        self.sqr11 = self.sqr11.to_dictionary()
        self.sqr12 = Square(1, 2, 3, 4)
        self.sqr12 = self.sqr12.to_dictionary()
        self.sqrStr = Square.to_json_string([self.sqr11, self.sqr12])
        self.sqrObj = Square.from_json_string(self.sqrStr)

        self.assertEqual(
                self.sqrObj,
                [{'x': 5, 'id': 7, 'size': 4, 'y': 6},
                    {'x': 2, 'id': 4, 'size': 1, 'y': 3}])

    def test_from_json_string_sqr_type(self):
        """Checks the type of object returned"""
        self.sqr13 = Square(4, 5, 6, 7)
        self.sqr13 = self.sqr13.to_dictionary()
        self.sqrStr = Square.to_json_string([self.sqr13])
        self.sqrObj = Square.from_json_string(self.sqrStr)

        self.assertTrue(type(self.sqrObj) == list)

    def test_from_json_string_excess_args(self):
        """Checks for errors when no arg is given"""
        with self.assertRaises(TypeError):
            Square.from_json_string([], '2')
