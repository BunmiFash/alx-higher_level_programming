#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def setUp(self):
        self.list1 = [1, 2, 3, 4, 7, 10]
        self.list2 = [10, 20, 90]
        self.list3 = [1, 2, 10.9, 5]
        self.list4 = [2, "school", 100, "hope"]
        self.list5 = [[1, 3, 4], 10, "str"]
        self.list6 = [2, 10, {"A": "dICT"}]
        self.list7 = []

    def tearDown(self):
        pass

    def test_max_num_int(self):
        self.assertEqual(max_integer(self.list1), 10)
        self.assertEqual(max_integer(self.list2), 90)

    def test_max_num_float(self):
        self.assertEqual(max_integer(self.list3), 10.9)

    def test_max_num_str(self):
        self.assertRaises(TypeError, max_integer, self.list4)

    def test_max_num_struct(self):
        self.assertRaises(TypeError, max_integer, self.list5)
        self.assertRaises(TypeError, max_integer, self.list6)

    def test_max_num_none(self):
        self.assertTrue(max_integer, self.list7)
