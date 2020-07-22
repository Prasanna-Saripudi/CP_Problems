# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).
# author: Prasanna Saripudi
import math


def nthpronicnumber(n):
    # nth number would be n*(n+1)
    # return n*(n+1)
    # otherwise need to check and iterate to see if a number is pronic or not
    count, value = 0, 0
    while count < n:
        value += 1
        if isPronic(value):
            count += 1
    return value


def isPronic(num):
    for i in range(int(math.sqrt(num))+1):
        if i * (i + 1) == num:
            return True
    return False
