# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
# author: Prasanna Saripudi
import math

# perfect squares are the squares of whole numbers like 1,4,9,16, etc
# for the '100' case, need to check if dat string can b a number


def isperfectsquare(n):
    if not isinstance(n, str) or n.isdigit():
        if isinstance(n, str):
            n = int(n)
        if n >= 0:
            root = math.sqrt(n)
            print(root)
            if root ** 2 == n and '0' == str(root)[-1]:
                return True
    return False
