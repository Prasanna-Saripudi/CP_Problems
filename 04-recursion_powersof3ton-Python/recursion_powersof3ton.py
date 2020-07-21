# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.
# author: Prasanna Saripudi
import math


def recursion_powersof3ton(n):
    if n < 1:
        return None
    elif n == 1:
        return [1]
        l = rec_power3(n, [])
        l.sort()
        return l


def rec_power3(n, listi):
    if n < 1:
        return listi
    # converting if decimal to int
    n = int(n // 1)
    # if we dont know the power of a number like 6^? = 36 , then wee can find that value using logs
    # log(base 6)36 = 2 ., also 6^2=36
    if math.isclose(math.log(n, 3), n):
        print(n)
        listi.append(n)
    return rec_power3(n - 1, listi)
