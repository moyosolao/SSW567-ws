# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    print(f"Classifying triangle with sides: a={a}, b={b}, c={c}")

    # Verify that all inputs are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        print("InvalidInput: One or more sides are not integers.")
        return 'InvalidInput'

    # Check if side lengths are within the valid range (1 to 200)
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        print("InvalidInput: One or more sides are out of the valid range (1-200).")
        return 'InvalidInput'

    # Check for the triangle inequality theorem
    # The sum of any two sides must be greater than the third side
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("NotATriangle: Triangle inequality theorem violated.")
        return 'NotATriangle'

    # Check for Equilateral Triangle (all sides equal)
    if a == b and b == c:
        print("Equilateral: All sides are equal.")
        return 'Equilateral'

    # Check for Right Triangle using Pythagoras' theorem
    # First, identify the longest side to be the potential hypotenuse
    sides = sorted([a, b, c])
    print(f"Sides sorted for right triangle check: {sides}")
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("Right: Triangle satisfies Pythagoras' theorem.")
        return 'Right'

    # Check for Isosceles Triangle (exactly two sides equal)
    if a == b or a == c or b == c:
        print("Isosceles: Exactly two sides are equal.")
        return 'Isosceles'

    # If none of the above, it's a Scalene Triangle (all sides different)
    print("Scalene: All sides are different.")
    return 'Scalene'
