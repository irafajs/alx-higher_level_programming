#!/usr/bin/python3
"""
Shebang to create python script
"""


import unittest
from models.square import Square


class test_Square(unittest.TestCase):
    """class test_Base to test"""
    def test_int(self):
        """test the square method"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_size(self):
        """test the size setter"""
        s2 = Square(100)
        self.assertEqual(s2.size, 100)

    def test_error_c(self):
        """to check if the value is true"""
        s3 = Square(2)
        with self.assertRaises(TypeError):
            s3.size = "9"

    def test_update(self):
        """to test square update method"""
        s4 = Square(9)
        s4u = s4.update(size=7, id=89, y=1)
        self.assertNotEqual(s4u, "(89) 12/1 - 7")


if __name__ == '__main__':
    unittest.main()
