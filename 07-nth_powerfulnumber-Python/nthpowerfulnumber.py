# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
# author: Prasanna Saripudi
import math


def nthpowerfulnumber(n):
    count, value = 0, 1
    while count < n:
        value += 1
        if primeFactors(value):
            count += 1
    return value


def primeFactors(num):
    # finding all the prime factors
    deg = 0
    while num % 2 == 0:
        deg += 1
        num //= 2
    if deg == 1:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        deg = 0
        while num % i == 0:
            deg += 1
            num = num // i
        if deg == 1:
            return False
        # since primes cant have prime factors., this is
        # just to make sure that num isnt the same after checking for prime factors
    # prime number will be the same after all this, but else it would be 1
    return num == 1
