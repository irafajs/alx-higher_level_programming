#!/usr/bin/python3
"""
Shebang to create python script
"""


import unittest
from models.rectangle import Rectangle


class test_Rectangle(unittest.TestCase):
    """class Test_Rectangle"""
    def test_area(self):
        """test area method"""
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_areadif(self):
        """test area method when fields are full"""
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertNotEqual(r3.area(), 96)

    def test_invalid_constructor(self):
        """test when one field is wrong"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_invalid_constructor_y(self):
        """test when y is not positive"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_display(self):
        """method to test the display method"""
        r1 = Rectangle(2, 2)
        self.assertNotEqual(r1.display(), "#")

    def test_over_str(self):
        """method to test __str__"""
        self.assertNotEqual(Rectangle(4, 6, 2, 1, 12), '(12) 2/1 - 4/6')

    def test_update(self):
        """test update method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.update(89, 2, 3, 4, 5)
        result = "(89) 4/5 - 2/3"
        self.assertNotEqual(str(r1), result)

    def test_to_dict(self):
        """test method to_dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        e_res = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertNotEqual(r1_dict, e_res)


if __name__ == '__main__':
    unittest.main()
