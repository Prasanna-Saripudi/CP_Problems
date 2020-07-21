# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.
# author: Prasanna Saripudi

def recursion_powersof3ton(n):
    if n < 1:
        return None
    elif n == 1:
        return [1]
    # converting if decimal to int
    n = int(n // 1)
    if n % 3 == 0:
        return recursion_powersof3ton(n - 1) + [n]
    else:
        return recursion_powersof3ton(n-1)
