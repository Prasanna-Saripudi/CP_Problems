# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.
# author: Prasanna Saripudi

def nthautomorphicnumbers(n):
    count, value = 1, 0
    while count < n:
        value += 1
        if isAutomorphic(value):
            count += 1
    return value


def isAutomorphic(num):
    sqr = str(num ** 2)
    return num == int(sqr[len(sqr)-len(str(num)):])
