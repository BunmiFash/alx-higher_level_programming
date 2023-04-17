#!/usr/bin/python3

"""Test Cases for test_square Module"""

import unittest
from models.square import Square
import io
from unittest.mock import patch


class TestSquareModule(unittest.TestCase):
    """Test cases for all methods"""

    def setUp(self):
        """Create instances"""
        pass

    def tearDown(self):
        """Delete instances"""
        pass

    def test_sqr_all_attr(self):
        """All attributes present"""
        self.sqr1 = Square(4, 2, 3, 7)
        self.assertEqual(self.sqr1.size, 4)
        self.assertEqual(self.sqr1.x, 2)
        self.assertEqual(self.sqr1.y, 3)
        self.assertEqual(self.sqr1.id, 7)

    def test_sqr_size(self):
        """Only size attribute present"""
        self.sqr2 = Square(5)
        self.assertEqual(self.sqr2.size, 5)
        self.assertEqual(self.sqr2.x, 0)
        self.assertEqual(self.sqr2.y, 0)
        self.assertEqual(self.sqr2.id, 1)

    def test_sqr_size_x(self):
        """Size and x attributes present"""
        self.sqr3 = Square(5, 3)
        self.assertEqual(self.sqr3.size, 5)
        self.assertEqual(self.sqr3.x, 3)
        self.assertEqual(self.sqr3.y, 0)
        self.assertEqual(self.sqr3.id, 138)

    def test_sqr_size_x_y(self):
        """Size and x and y attributes present"""
        self.sqr4 = Square(5, 3, 6)
        self.assertEqual(self.sqr4.size, 5)
        self.assertEqual(self.sqr4.x, 3)
        self.assertEqual(self.sqr4.y, 6)
        self.assertEqual(self.sqr4.id, 139)

    def test_sqr_size_str(self):
        """Size is a string"""
        with self.assertRaises(TypeError):
            self.sqr5 = Square("school", 3, 4, 5)

    def test_sqr_x_str(self):
        """x is a string"""
        with self.assertRaises(TypeError):
            self.sqr6 = Square(5, "school", 4, 5)

    def test_sqr_y_str(self):
        """y is a string"""
        with self.assertRaises(TypeError):
            self.sqr7 = Square(5, 3, "4", 5)

    def test_sqr_size_negative(self):
        """size is a negative value"""
        with self.assertRaises(ValueError):
            self.sqr8 = Square(-5, 3, 4, 5)

    def test_sqr_x_negative(self):
        """x is a negative value"""
        with self.assertRaises(ValueError):
            self.sqr9 = Square(5, -6, 4, 5)

    def test_sqr_y_negative(self):
        """y is a negative value"""
        with self.assertRaises(ValueError):
            self.sqr10 = Square(5, 3, -4, 5)

    def test_sqr_size_zero(self):
        """size is zero"""
        with self.assertRaises(ValueError):
            self.sqr11 = Square(0, 3, 4, 5)

    def test_sqr_size_list(self):
        """Size is a list"""
        with self.assertRaises(TypeError):
            self.sqr12 = Square([10, 'school'], 3, 4, 5)

    def test_sqr_x_list(self):
        """x is a list"""
        with self.assertRaises(TypeError):
            self.sqr13 = Square(5, ["school", 67], 4, 5)

    def test_sqr_y_list(self):
        """y is a list"""
        with self.assertRaises(TypeError):
            self.sqr14 = Square(5, 3, ["4"], 5)

    def test_sqr_size_tuple(self):
        """Size is a tuple"""
        with self.assertRaises(TypeError):
            self.sqr15 = Square((10, 'school'), 3, 4, 5)

    def test_sqr_x_tuple(self):
        """x is a tuple"""
        with self.assertRaises(TypeError):
            self.sqr16 = Square(5, ("school", 67), 4, 5)

    def test_sqr_y_tuple(self):
        """y is a tuple"""
        with self.assertRaises(TypeError):
            self.sqr17 = Square(5, 3, ("4"), 5)

    def test_sqr_size_dictt(self):
        """Size is a dict"""
        with self.assertRaises(TypeError):
            self.sqr18 = Square({10: 'school'}, 3, 4, 5)

    def test_sqr_x_dict(self):
        """x is a dict"""
        with self.assertRaises(TypeError):
            self.sqr19 = Square(5, {"school": 67}, 4, 5)

    def test_sqr_y_dict(self):
        """y is a dict"""
        with self.assertRaises(TypeError):
            self.sqr20 = Square(5, 3, {"4": 10}, 5)

    def test_sqr_size_float(self):
        """size is a float value"""
        with self.assertRaises(TypeError):
            self.sqr21 = Square(-5.78, 3, 4, 5)

    def test_sqr_x_float(self):
        """x is a float value"""
        with self.assertRaises(TypeError):
            self.sqr22 = Square(5, 6.45, 4, 5)

    def test_sqr_y_float(self):
        """y is a float value"""
        with self.assertRaises(TypeError):
            self.sqr23 = Square(5, 3, 4.78, 5)

    def test_sqr_size_bool(self):
        """Size is a bool"""
        with self.assertRaises(TypeError):
            self.sqr24 = Square(True, 3, 4, 5)

    def test_sqr_x_bool(self):
        """x is a bool"""
        with self.assertRaises(TypeError):
            self.sqr25 = Square(5, False, 4, 5)

    def test_sqr_y_bool(self):
        """y is a bool"""
        with self.assertRaises(TypeError):
            self.sqr26 = Square(5, 3, True, 5)

    """ AREA TEST CASES"""

    def test_sqr_area(self):
        """Test case for area of a square"""
        self.sqr27 = Square(10, 3, 4, 9)
        self.area = self.sqr27.area()
        self.assertTrue(self.area == 100)

    """
    TEST CASES FOR display()
    """

    def test_sqr_display_with_x_y(self):
        """Displaying square with x, y"""
        self.sqr28 = Square(4, 3, 2, 5)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_out:
            self.res1 = self.sqr28.display()
            self.expected1 = "\n\n   ####\n   ####\n   ####\n   ####\n"
            self.assertEqual(mock_out.getvalue(), self.expected1)

    def test_sqr_display_with_no_x_y(self):
        """Displaying square with only size"""
        self.sqr29 = Square(5, 0, 0, 1)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_output:
            self.res2 = self.sqr29.display()
            self.expected2 = "#####\n#####\n#####\n#####\n#####\n"
            self.assertEqual(mock_output.getvalue(), self.expected2)

    """
    TEST CASES FOR ___str__()
    """

    def test_sqr_str_(self):
        """String representation of square, all attr"""
        self.sqr30 = Square(10, 2, 3, 5)
        self.str1 = self.sqr30.__str__()
        self.assertEqual(self.str1, "[Square] (5) 2/3 - 10")

    def test_sqr_str_size_only(self):
        """String representation of square, only size"""
        self.sqr31 = Square(1)
        self.str2 = self.sqr31.__str__()
        self.assertEqual(self.str2, "[Square] (140) 0/0 - 1")

    def test_sqr_str_size_x(self):
        """String representation of square: size and x"""
        self.sqr32 = Square(2, 3)
        self.str3 = self.sqr32.__str__()
        self.assertEqual(self.str3, "[Square] (141) 3/0 - 2")

    def test_sqr_str_size_x_y(self):
        """String representation of square: size and x and y"""
        self.sqr33 = Square(3, 4, 5)
        self.str4 = self.sqr33.__str__()
        self.assertEqual(self.str4, "[Square] (142) 4/5 - 3")

    """
    TEST CASES FOR UPDATE ARGS METHOD
    """

    def test_sqr_update_args(self):
        """Square Update args of all attributes"""
        self.sqr34 = Square(5, 2, 3, 5)
        self.newSqr1 = self.sqr34.update(6, 3, 4, 8)
        self.assertEqual(self.sqr34.id, 6)
        self.assertEqual(self.sqr34.size, 3)
        self.assertEqual(self.sqr34.x, 4)
        self.assertEqual(self.sqr34.y, 8)

    def test_sqr_update_arg_no_id(self):
        """Update square with no id"""
        self.sqr35 = Square(5, 2, 3, 5)
        self.newSqr2 = self.sqr35.update()
        self.assertEqual(self.sqr35.id, 5)

    def test_sqr_update_arg_id(self):
        """Update square with id"""
        self.sqr36 = Square(5, 2, 3, 5)
        self.newSqr3 = self.sqr36.update(23)
        self.assertEqual(self.sqr36.id, 23)

    def test_sqr_update_arg_id_size(self):
        """Update square with id, size"""
        self.sqr37 = Square(5, 2, 3, 5)
        self.newSqr4 = self.sqr37.update(23, 3)
        self.assertEqual(self.sqr37.size, 3)

    def test_sqr_update_arg_id_size_x(self):
        """Update square with id, size, x"""
        self.sqr38 = Square(5, 2, 3, 5)
        self.newSqr5 = self.sqr38.update(23, 3, 10)
        self.assertEqual(self.sqr38.x, 10)

    """
    TEST CASES FOR UPDATE KWARGS METHOD
    """

    def test_sqr_update_kwarg_all_attr(self):
        self.sqr39 = Square(5, 2, 3, 5)
        self.newSqr6 = self.sqr39.update(size=4, id=12, x=2, y=1)
        self.assertTrue(self.sqr39.id == 12)
        self.assertTrue(self.sqr39.x == 2)
        self.assertTrue(self.sqr39.y == 1)
        self.assertTrue(self.sqr39.size == 4)

    def test_sqr_update_kwarg_id(self):
        self.sqr40 = Square(5, 2, 3, 5)
        self.newSqr7 = self.sqr40.update(id=9)
        self.assertTrue(self.sqr40.id == 9)

    def test_sqr_update_kwarg_size(self):
        self.sqr41 = Square(5, 2, 3, 5)
        self.newSqr8 = self.sqr41.update(size=10)
        self.assertTrue(self.sqr41.size == 10)

    def test_sqr_update_kwarg_x(self):
        self.sqr42 = Square(5, 2, 3, 5)
        self.newSqr9 = self.sqr42.update(x=9)
        self.assertTrue(self.sqr42.x == 9)

    def test_sqr_update_kwarg_y(self):
        self.sqr43 = Square(5, 2, 3, 5)
        self.newSqr10 = self.sqr43.update(y=28)
        self.assertTrue(self.sqr43.y == 28)

    """
    TEST CASES FOR to_dictionary()
    """
    def test_sqr_dict(self):
        self.sqr44 = Square(10, 4, 5, 2)
        self.dict1 = self.sqr44.to_dictionary()
        self.assertEqual(
                self.dict1, {'id': 2, 'x': 4, 'size': 10, 'y': 5}
                )

    def test_sqr_dict_no_id(self):
        self.sqr45 = Square(10, 4, 5)
        self.dict2 = self.sqr45.to_dictionary()
        self.assertEqual(
                self.dict2, {'id': 135, 'x': 4, 'size': 10, 'y': 5})

    def test_sqr_dict_no_id_y(self):
        self.sqr46 = Square(10, 4)
        self.dict3 = self.sqr46.to_dictionary()
        self.assertEqual(
                self.dict3, {'id': 136, 'x': 4, 'size': 10, 'y': 0})

    def test_sqr_dict_no_id_y_x(self):
        self.sqr47 = Square(10)
        self.dict4 = self.sqr47.to_dictionary()
        self.assertEqual(
                self.dict4, {'id': 137, 'x': 0, 'size': 10, 'y': 0})

    def test_sqr_dict_all(self):
        """Converts all attributes to  dictionary"""
        self.sqr48 = Square(7, 4, 2, 3)
        self.dict5 = self.sqr48.to_dictionary()

        self.assertTrue(self.dict5["id"] == 3)
        self.assertTrue(self.dict5["x"] == 4)
        self.assertTrue(self.dict5["y"] == 2)
        self.assertTrue(self.dict5["size"] == 7)

    def test_sqr_type_dict(self):
        """Checks the type returned by to_dictionary"""
        self.sqr49 = Square(7, 4, 2, 3)
        self.dict6 = self.sqr49.to_dictionary()

        self.assertTrue(type(self.dict6) == dict)

    """
    TEST FOR INCOMPLETE ARGUMENTS
    """
    def test_sqr_size(self):
        """Checks for the absence of size attribute"""
        with self.assertRaises(TypeError):
            self.sqr50 = Square()

    """
    TEST DOCUMENTATION LENGTH
    """
    def test_str_doc(self):
        """Checks for the length of the module documentation"""
        self.doc_length = len(Square.__doc__)
        self.assertGreaterEqual(self.doc_length, 1)
