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
        flag = True
        value += 1
        for i in primeFactors(n):
            if n % i != 0 or n % (i * i) != 0:
                flag = False
                break
        if flag:
            count += 1
    return value


def primeFactors(num):
    # finding all the prime factors
    pFactrs = set()
    while num % 2 == 0:
        pFactrs.add(2)
        num = num // 2
    for i in range(2, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            pFactrs.add(i)
            num = num // i
    if num > 2:
        pFactrs.add(num)
    return list(pFactrs)
