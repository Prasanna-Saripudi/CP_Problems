# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
# author: Prasanna Saripudi
import math
from math import isclose


def isrighttriangle(x1, y1, x2, y2, x3, y3):
    # calculate the sides of traingle
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x1, y1, x3, y3)
    sides = [a, b, c]
    maxSideInt = sides.index(max(sides))
    remSides = [i for i in [0, 1, 2] if i != maxSideInt]
    # check if hyp sqr = sum of sqr of two rem
    if isclose(sides[remSides[0]]**2 + sides[remSides[1]]**2, sides[maxSideInt]**2):
        return True
    return False


def distance(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
