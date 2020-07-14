# Write the function bonusFindIntRoots(a,b,c) that takes
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that
# the roots are all integers. Your function should return these 2 int roots
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2
# author: Prasanna Saripudi
import math

# formula for real roots ax ^ 2 + bx + c; (-b+-sqrt(b^2-4ac))/2a


def fun_find_int_roots(a, b, c):
    const = math.sqrt(b * b - 4 * a * c)
    x1 = int((-b - const) / (2 * a))
    x2 = int((-b+const)/(2*a))
    return x1, x2
