#!/usr/bin/python3
"""
Shebang to create python script
"""


import unittest
from models.base import Base


class test_Base(unittest.TestCase):
    """class test_Base to test"""
    def test_init(self, id=None):
        """to test __init__ method"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(12)
        self.assertEqual(b2.id, 12)


if __name__ == '__main__':
    unittest.main()
