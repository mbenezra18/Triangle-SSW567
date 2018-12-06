# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk

@author: Michayla Ben-Ezra
Updated on September 9, 2018

"""

import unittest
from unittest.mock import create_autospec

from triangle_2 import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3, 4, 5), 'This is a right triangle.', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5, 3, 4), 'This is a right triangle.', '5,3,4 is a Right triangle')
        
    def testEquilateralTrianglesA(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'This is an equilateral triangle.', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classify_triangle(15, 15, 15), 'This is an equilateral triangle.', '1,1,1 should be equilateral')

    def testScaleneTrianglesA(self):
        self.assertEqual(classify_triangle(13, 14, 9), 'This is a scalene triangle.', '13,14,9 should be scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classify_triangle(16, 14, 9), 'This is a scalene triangle.', '13,14,9 should be scalene')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classify_triangle(4, 4, 1), 'This is an isosceles triangle.', '4,4,1 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classify_triangle(5, 5, 2), 'This is an isosceles triangle.', '4,4,1 should be isosceles')

    def testNotATriangleA(self):
        self.assertEqual(classify_triangle(1, 1, 199), 'This is not a triangle.', '1,1,199 should be NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classify_triangle(15, 8, 4), 'This is not a triangle.', '15,8,4 should be NotATriangle')

    def testInvalidInputA(self):
        self.assertEqual(classify_triangle(15, 2000, -1000), 'Invalid Input', '15,2000,-1000 should be InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classify_triangle(1, 2, 'three'), 'Invalid Input', '1,2,three should be InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

