#!/usr/bin/python3


"""Test Module for class Rectangle"""

import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle class"""
    def setUp(self):
        """Set Up Instances"""

        self.rect1 = Rectangle(23, 20, 2, 4)
        self.rect2 = Rectangle(12, 30, 12, 9, 22)
        self.rect3 = Rectangle(10, 1)

    def tearDown(self):
        """Remove instances"""
        del self.rect1
        del self.rect2
        del self.rect3

    def test_rect_no_id(self):
        """Test all attributes, id = none"""
        self.assertEqual(self.rect1.width, 23)
        self.assertEqual(self.rect1.height, 20)
        self.assertEqual(self.rect1.x, 2)
        self.assertEqual(self.rect1.y, 4)
        self.assertEqual(self.rect1.id, 71)

    def test_rect_all_attr(self):
        """Test all attributes present"""
        self.assertEqual(self.rect2.width, 12)
        self.assertEqual(self.rect2.height, 30)
        self.assertEqual(self.rect2.x, 12)
        self.assertEqual(self.rect2.y, 9)
        self.assertEqual(self.rect2.id, 22)

    def test_rect_attr(self):
        """X, y, id absent"""
        self.assertEqual(self.rect3.width, 10)
        self.assertEqual(self.rect3.height, 1)
        self.assertEqual(self.rect3.x, 0)
        self.assertEqual(self.rect3.y, 0)
        self.assertEqual(self.rect3.id, 22)

    def test_rect_negative_x(self):
        """x is -ve"""
        with self.assertRaises(ValueError):
            self.rect4 = Rectangle(10, 5, -2, 5, 7)

    def test_rect_negative_y(self):
        """y is -ve"""
        with self.assertRaises(ValueError):
            self.rect5 = Rectangle(13, 3, 2, -4, 2)

    def test_rect_x_str(self):
        """x is string"""
        with self.assertRaises(TypeError):
            self.rect6 = Rectangle(10, 5, "school", 5, 7)

    def test_rect_y_str(self):
        """y is string"""
        with self.assertRaises(TypeError):
            self.rect7 = Rectangle(13, 3, 2, "alx", 2)

    def test_rect_negative_width(self):
        """width is -ve"""
        with self.assertRaises(ValueError):
            self.rect8 = Rectangle(-10, 5, 2, 5, 7)

    def test_rect_negative_height(self):
        """height is -ve"""
        with self.assertRaises(ValueError):
            self.rect9 = Rectangle(13, -33, 2, 4, 2)

    def test_rect_width_zero(self):
        """width is zero"""
        with self.assertRaises(ValueError):
            self.rect10 = Rectangle(0, 5, 2, 5, 7)

    def test_rect_height_zero(self):
        """height is zero"""
        with self.assertRaises(ValueError):
            self.rect11 = Rectangle(13, 0, 2, 4, 2)

    def test_rect_str_width(self):
        """width is a string"""
        with self.assertRaises(TypeError):
            self.rect12 = Rectangle("code", 5, 2, 5, 7)

    def test_rect_str_height(self):
        """height is string"""
        with self.assertRaises(TypeError):
            self.rect13 = Rectangle(13, "tech", 2, 4, 2)

    def test_rect_x_dict(self):
        """x is a dict"""
        with self.assertRaises(TypeError):
            self.rect14 = Rectangle(10, 5, {"school": 10}, 5, 7)

    def test_rect_y_dict(self):
        """y is a dict"""
        with self.assertRaises(TypeError):
            self.rect15 = Rectangle(13, 3, 2, {"alx": 12}, 2)

    def test_rect_dict_width(self):
        """width is a dict"""
        with self.assertRaises(TypeError):
            self.rect16 = Rectangle({"code": 12}, 5, 2, 5, 7)

    def test_rect_dict_height(self):
        """height is a dict"""
        with self.assertRaises(TypeError):
            self.rect17 = Rectangle(13, {"tech": "50"}, 2, 4, 2)

    def test_rect_x_list(self):
        """x is a list"""
        with self.assertRaises(TypeError):
            self.rect18 = Rectangle(10, 5, [2, 10], 5, 7)

    def test_rect_y_list(self):
        """y is a list"""
        with self.assertRaises(TypeError):
            self.rect19 = Rectangle(13, 3, 2, ["alx", 12], 2)

    def test_rect_list_width(self):
        """width is a list"""
        with self.assertRaises(TypeError):
            self.rect20 = Rectangle(["code", 12], 5, 2, 5, 7)

    def test_rect_list_height(self):
        """height is a listt"""
        with self.assertRaises(TypeError):
            self.rect21 = Rectangle(13, [21, "50"], 2, 4, 2)

    def test_rect_x_tuple(self):
        """x is a tuple"""
        with self.assertRaises(TypeError):
            self.rect22 = Rectangle(10, 5, (2, 10), 5, 7)

    def test_rect_y_tuple(self):
        """y is a tuple"""
        with self.assertRaises(TypeError):
            self.rect23 = Rectangle(13, 3, 2, ("alx", 12), 2)

    def test_rect_tuple_width(self):
        """width is a tuple"""
        with self.assertRaises(TypeError):
            self.rect24 = Rectangle(("code", 12), 5, 2, 5, 7)

    def test_rect_tuple_height(self):
        """height is a tuple"""
        with self.assertRaises(TypeError):
            self.rect25 = Rectangle(13, (21, "50"), 2, 4, 2)

    def test_rect_x_float(self):
        """x is a float"""
        with self.assertRaises(TypeError):
            self.rect26 = Rectangle(10, 5, 2.10, 5, 7)

    def test_rect_y_float(self):
        """y is a float"""
        with self.assertRaises(TypeError):
            self.rect27 = Rectangle(13, 3, 2, 1.2, 2)

    def test_rect_float_width(self):
        """width is a float"""
        with self.assertRaises(TypeError):
            self.rect28 = Rectangle(1.2, 5, 2, 5, 7)

    def test_rect_float_height(self):
        """height is a float"""
        with self.assertRaises(TypeError):
            self.rect29 = Rectangle(13, 2.50, 2, 4, 2)

    def test_rect_x_bool(self):
        """x is a bool"""
        with self.assertRaises(TypeError):
            self.rect200 = Rectangle(10, 5, True, 5, 7)

    def test_rect_y_bool(self):
        """y is a bool"""
        with self.assertRaises(TypeError):
            self.rect201 = Rectangle(13, 3, 2, False, 2)

    def test_rect_bool_width(self):
        """width is a bool"""
        with self.assertRaises(TypeError):
            self.rect202 = Rectangle(True, 5, 2, 5, 7)

    def test_rect_bool_height(self):
        """height is a bool"""
        with self.assertRaises(TypeError):
            self.rect203 = Rectangle(13, False, 2, 4, 2)

    """
    AREA TEST CASE
    """

    def test_rect_area(self):
        """area test case"""
        self.area1 = self.rect1.area()
        self.assertTrue(self.area1 == 460)

    """
    DISPLAY TEST CASE
    """
    def test_rect_display_all_attr(self):
        """Test to print out a rectangle with #"""
        self.r1 = Rectangle(4, 3, 3, 2, 9)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_out:
            self.disp = self.r1.display()
            self.expect = "\n\n   ####\n   ####\n   ####\n"
            self.assertEqual(mock_out.getvalue(), self.expect)

    def test_rect_display_width_height(self):
        """Test to print out rectangle with #"""
        self.r2 = Rectangle(4, 2)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_output:
            self.disp2 = self.r2.display()
            self.expect2 = "####\n####\n"
            self.assertEqual(mock_output.getvalue(), self.expect2)

    """
    TEST CASES FOR __str__()
    """

    def test_str_(self):
        """Overriding the __str__()"""
        self.res1 = self.rect2.__str__()
        self.resEx = "[Rectangle] (22) 12/9 - 12/30"
        self.assertEqual(self.res1, self.resEx)

    def test__str__no_id(self):
        """Overriding string with no id provided"""
        self.rectt = Rectangle(4, 2, 7, 2)
        self.res2 = self.rectt.__str__()
        self.resExp = "[Rectangle] (13) 7/2 - 4/2"
        self.assertEqual(self.res2, self.resExp)

    def test__str__no_y_id(self):
        """Overridng string with no y and id"""
        self.rect29 = Rectangle(10, 4, 6)
        self.res3 = self.rect29.__str__()
        self.resExp1 = "[Rectangle] (16) 6/0 - 10/4"
        self.assertEqual(self.res3, self.resExp1)

    def test_str__no__x_y_id(self):
        """Overridng string with no x, y and id"""
        self.rect30 = Rectangle(10, 4)
        self.res4 = self.rect30.__str__()
        self.resExp2 = "[Rectangle] (140) 0/0 - 10/4"
        self.assertEqual(self.res4, self.resExp2)

    """
    TEST CASES FOR UPDATE WITH ARGS
    """

    def test_rect_update_no_id(self):
        """Update value of id == None"""
        self.rect30 = Rectangle(10, 10, 10, 10)
        self.newRect = self.rect30.update()
        self.assertTrue(self.rect30.id == 1)

    def test_rect_update_no_id(self):
        """Update the value id with an int value"""
        self.rect32 = Rectangle(10, 10, 10, 10)
        self.newRect3 = self.rect32.update(89)
        self.assertTrue(self.rect32.id == 89)

    def test_rect_update_width(self):
        """Update the value width"""
        self.rect31 = Rectangle(3, 12, 3, 4, 2)
        self.newRect2 = self.rect31.update(5, 3)
        self.assertTrue(self.rect31.width == 3)

    def test_rect_update_height(self):
        """Update the value of height"""
        self.rect33 = Rectangle(3, 12, 3, 4, 2)
        self.newRect3 = self.rect33.update(5, 3, 5)
        self.assertTrue(self.rect33.height == 5)

    def test_rect_update_x(self):
        """Update the value of x"""
        self.rect34 = Rectangle(3, 12, 3, 4, 2)
        self.newRect4 = self.rect34.update(5, 3, 5, 5)
        self.assertTrue(self.rect34.x == 5)

    def test_rect_update_y(self):
        """Update the value of y"""
        self.rect35 = Rectangle(3, 12, 3, 4, 2)
        self.newRect5 = self.rect35.update(5, 3, 5, 5, 6)
        self.assertTrue(self.rect35.y == 6)

    """
    TEST CASES FOR UPDATE WITH KWARGS
    """

    def test_rect_update_kwargs_id(self):
        """Update the value of id with kwargs"""
        self.rect36 = Rectangle(3, 12, 3, 4, 2)
        self.newRect6 = self.rect36.update(id=10)
        self.assertTrue(self.rect36.id == 10)

    def test_rect_update_kwargs_width(self):
        """Update the value of width with kwargs"""
        self.rect37 = Rectangle(3, 12, 3, 4, 2)
        self.newRect7 = self.rect37.update(width=10)
        self.assertTrue(self.rect37.width == 10)

    def test_rect_update_kwargs_height(self):
        """Update the value of height with kwargs"""
        self.rect38 = Rectangle(3, 12, 3, 4, 2)
        self.newRect8 = self.rect38.update(height=10)
        self.assertTrue(self.rect38.height == 10)

    def test_rect_update_kwargs_x(self):
        """Update the value of x with kwargs"""
        self.rect39 = Rectangle(3, 12, 3, 4, 2)
        self.newRect9 = self.rect39.update(x=10)
        self.assertTrue(self.rect39.x == 10)

    def test_rect_update_kwargs_y(self):
        """Update the value of y with kwargs"""
        self.rect40 = Rectangle(3, 12, 3, 4, 2)
        self.newRect10 = self.rect40.update(y=10)
        self.assertTrue(self.rect40.y == 10)

    def test_rect_update_kwargs_all_attr(self):
        """Updates all attributes"""
        self.rect41 = Rectangle(3, 12, 3, 4, 2)
        self.newRec11 = self.rect41.update(
                height=8, y=6, x=9, width=23, id=23
                )
        self.assertEqual(self.rect41.width, 23)
        self.assertEqual(self.rect41.height, 8)
        self.assertEqual(self.rect41.id, 23)
        self.assertEqual(self.rect41.y, 6)
        self.assertEqual(self.rect41.x, 9)

    def test_rect_update_kwargs_no_id(self):
        """Updates all attributes except id"""
        self.rect42 = Rectangle(3, 12, 3, 4, 2)
        self.newRec12 = self.rect42.update(
                height=8, y=6, x=9, width=23
                )
        self.assertEqual(self.rect42.width, 23)
        self.assertEqual(self.rect42.height, 8)
        self.assertEqual(self.rect42.id, 2)
        self.assertEqual(self.rect42.y, 6)
        self.assertEqual(self.rect42.x, 9)

    """
    TEST CASES FOR dictionary()
    """
    def test_rect_dict_all_attr(self):
        """Converts all attributes to a dictionary"""
        self.rect43 = Rectangle(7, 4, 2, 3, 5)
        self.dict1 = self.rect43.to_dictionary()
        self.assertEqual(
                self.dict1,
                {'x': 2, 'y': 3, 'id': 5, 'height': 4, 'width': 7})

    def test_rect_dict_no_id(self):
        """Converts all attributes to a dictionary"""
        self.rect44 = Rectangle(7, 4, 2, 3)
        self.dict2 = self.rect44.to_dictionary()
        self.assertEqual(
                self.dict2,
                {'x': 2, 'y': 3, 'id': 35, 'height': 4, 'width': 7})

    def test_rect_dict_no_id_y(self):
        """Converts all attributes to a dictionary"""
        self.rect45 = Rectangle(7, 4, 2)
        self.dict3 = self.rect45.to_dictionary()
        self.assertEqual(
                self.dict3,
                {'x': 2, 'y': 0, 'id': 38, 'height': 4, 'width': 7})

    def test_rect_dict_no_id_y_y(self):
        """Converts all attributes to a dictionary"""
        self.rect46 = Rectangle(7, 4)
        self.dict4 = self.rect46.to_dictionary()
        self.assertEqual(
                self.dict4,
                {'x': 0, 'y': 0, 'id': 41, 'height': 4, 'width': 7})

    def test_rect_dict_all(self):
        """Converts all attributes to  dictionary"""
        self.rect47 = Rectangle(7, 4, 2, 3, 5)
        self.dict5 = self.rect47.to_dictionary()

        self.assertTrue(self.dict5["id"] == 5)
        self.assertTrue(self.dict5["x"] == 2)
        self.assertTrue(self.dict5["y"] == 3)
        self.assertTrue(self.dict5["height"] == 4)
        self.assertTrue(self.dict5["width"] == 7)

    def test_rect_dict_type(self):
        """Checks the return type of to_dictionary()"""
        self.rect48 = Rectangle(7, 4, 2, 3, 5)
        self.dict6 = self.rect48.to_dictionary()
        self.assertTrue(type(self.dict6) == dict)

    """
    TEST FOR INCOMPLETE ARGUMENTS
    """
    def test_rect_no_width(self):
        """Checks for the absence of width"""
        with self.assertRaises(TypeError):
            self.rect49 = Rectangle()

    def test_rect_no_height(self):
        """Checks for the absence of height"""
        with self.assertRaises(TypeError):
            self.rect50 = Rectangle(12)

    """
    TEST DOCUMENTATION LENGTH
    """
    def test_rectangle_doc(self):
        self.doc_length = len(Rectangle.__doc__)
        self.assertGreaterEqual(self.doc_length, 1)
