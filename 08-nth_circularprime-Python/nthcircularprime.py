# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
# author: Prasanna Saripudi
import math


def nthcircularprime(n):
    count, value = 0, 2
    while count < n:
        value += 1
        if isCircularPrime(value):
            # print(value, count)
            count += 1
    return value


def isCircularPrime(num):
    if isPrime(num):
        numStr = str(num)
        for x in ['0', '2', '4', '6', '8']:
            if x in numStr:
                return False
            # checking for all the rotations if prime or not
        for i in range(len(numStr)):
            x = numStr[i:] + numStr[:i]
            if not isPrime(int(x)):
                return False
        return True
    return False


def isPrime(num):
    if num == 2 or num == 3:
        return True
    elif num <= 1 or num % 2 == 0 or num % 3 == 0:
        return False
        # optimizing the prime number checks for eg: 5 , 7 and 9 anyhow is a multipleof 3 ., so += 6
    for i in range(5, int(math.sqrt(num))+1, 6):
        if num % i == 0 or num % (i+2) == 0:
            return False
    return True
