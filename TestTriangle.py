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

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(15, 15, 15), 'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(13, 14, 9), 'Scalene', '13,14,9 should be scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(16, 14, 9), 'Scalene', '13,14,9 should be scalene')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(4, 4, 1), 'Isosceles', '4,4,1 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(4, 4, 1), 'Isosceles', '4,4,1 should be isosceles')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 199), 'NotATriangle', '1,1,199 should be NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(15, 8, 4), 'NotATriangle', '15,8,4 should be NotATriangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(15, 2000, -1000), 'InvalidInput', '15,2000,-1000 should be InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(1, 2, 'three'), 'InvalidInput', '1,2,three should be InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

