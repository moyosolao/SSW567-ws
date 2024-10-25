# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

print("Executing TestTriangle.py")

class TestTriangles(unittest.TestCase):
    # Test for Right Triangles
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 should be a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 should be a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6,8,10 should be a Right triangle')

    # Test for Equilateral Triangles
    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be Equilateral')
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be Equilateral')

    # Test for Isosceles Triangles
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 should be Isosceles')
        self.assertEqual(classifyTriangle(3, 4, 4), 'Isosceles', '3,4,4 should be Isosceles')
        self.assertEqual(classifyTriangle(4, 3, 4), 'Isosceles', '4,3,4 should be Isosceles')

    # Test for Scalene Triangles
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2,3,4 should be Scalene')
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene', '5,6,7 should be Scalene')
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10,11,12 should be Scalene')

    # Test for Not a Triangle
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1,1,3 is not a triangle')
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10,1,1 is not a triangle')
        self.assertEqual(classifyTriangle(1, 10, 1), 'NotATriangle', '1,10,1 is not a triangle')
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 is invalid input')
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput', '-1,2,3 is invalid input')

    # Test for Invalid Inputs
    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(201, 10, 10), 'InvalidInput', '201,10,10 exceeds maximum side length')
        self.assertEqual(classifyTriangle(10, 201, 10), 'InvalidInput', '10,201,10 exceeds maximum side length')
        self.assertEqual(classifyTriangle(10, 10, 201), 'InvalidInput', '10,10,201 exceeds maximum side length')
        self.assertEqual(classifyTriangle('a', 10, 10), 'InvalidInput', 'Non-integer input should be invalid')
        self.assertEqual(classifyTriangle(10, 'b', 10), 'InvalidInput', 'Non-integer input should be invalid')
        self.assertEqual(classifyTriangle(10, 10, 'c'), 'InvalidInput', 'Non-integer input should be invalid')
        self.assertEqual(classifyTriangle(10.5, 10, 10), 'InvalidInput', 'Float input should be invalid')
        self.assertEqual(classifyTriangle(10, 10.5, 10), 'InvalidInput', 'Float input should be invalid')
        self.assertEqual(classifyTriangle(10, 10, 10.5), 'InvalidInput', 'Float input should be invalid')

    # Test for Boundary Conditions
    def testBoundaryConditions(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', 'Minimum valid side lengths')
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', 'Maximum valid side lengths')
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', 'Sum of two sides equals the third side')

    # Test for Additional Right Triangles
    def testAdditionalRightTriangles(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 should be a Right triangle')
        self.assertEqual(classifyTriangle(9, 12, 15), 'Right', '9,12,15 should be a Right triangle')

    # Test for All Possible Orderings of Sides
    def testAllOrderings(self):
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', '5,5,5 should be Equilateral')
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be Isosceles')
        self.assertEqual(classifyTriangle(5, 8, 5), 'Isosceles', '5,8,5 should be Isosceles')
        self.assertEqual(classifyTriangle(8, 5, 5), 'Isosceles', '8,5,5 should be Isosceles')
        self.assertEqual(classifyTriangle(7, 24, 25), 'Right', '7,24,25 should be Right triangle')
        self.assertEqual(classifyTriangle(24, 7, 25), 'Right', '24,7,25 should be Right triangle')
        self.assertEqual(classifyTriangle(25, 24, 7), 'Right', '25,24,7 should be Right triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
