# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
# author: Prasanna Saripudi
import math


def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x1, y1, x3, y3)
    return traingleArea(s1, s2, s3)


def traingleArea(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))


def distance(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
