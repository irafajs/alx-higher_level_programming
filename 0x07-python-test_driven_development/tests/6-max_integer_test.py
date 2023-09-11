#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3,4, -100]), 4)

    def test_max_integer_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_1element(self):
        self.assertEqual(max_integer([10]), 10)
