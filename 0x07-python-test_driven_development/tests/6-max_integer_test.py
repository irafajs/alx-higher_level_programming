#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class to test using unittest module
    """
    def test_max_integer(self):
        """methods to test max int when passed mixed int"""
        self.assertEqual(max_integer([1, 2, 3, 4, -100, 10.7]), 10.7)

    def test_max_integer_empty(self):
        """method to test max int when list is empty"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_1element(self):
        """method to test max int when list has one element"""
        self.assertEqual(max_integer([10]), 10)

    def test_max_integer_atbegin(self):
        """method to test max int when max int is at the beginning"""
        self.assertEqual(max_integer([110, 2, 3, 4, -100, 10.7]), 110)

    def test_max_integer_inmid(self):
        """method to test max int when max int is in the middle"""
        self.assertEqual(max_integer([1, 2, 3, 300, 4, -100, 10.7]), 300)
