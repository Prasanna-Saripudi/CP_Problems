# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
# author: Prasanna Saripudi
import math


def fun_nth_uglynumber(n):
    count, value = 0, 1
    while count < n:
        value += 1
        if primeFactors(value):
            count += 1
    return value


def primeFactors(num):
    # checking if the num has only 2,3,5 as prime factors
    num = divideMax(num, 2)
    num = divideMax(num, 3)
    num = divideMax(num, 5)
    return num == 1


def divideMax(num, pf):
    while num % pf == 0:
        num //= pf
    return num
