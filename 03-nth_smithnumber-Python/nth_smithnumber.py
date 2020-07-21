# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
# author: Prasanna Saripudi
import math


def fun_nth_smithnumber(n):
    count, value = 0, 4
    # repeats until the count value
    while count < n:
        value += 1
        sumNum = sumdigits(value)
        pfactors = primeFactors(value)
        sumPrimefactrs = sum([sumdigits(x) for x in pfactors])
        if isComposite(value) and sumNum == sumPrimefactrs:
            count += 1
    return value


def primeFactors(num):
    # for finding the primeFactors
    pfactrs = []
    # checking 2 as a prime factor and number of 2's for that number as PF
    while num % 2 == 0:
        pfactrs.append(2)
        num = num / 2
    # checking for the primes in the same way
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            pfactrs.append(i)
            num = num / i
    if num > 2:
        pfactrs.append(int(num))
    return pfactrs


def isComposite(num):
    # to check if its composite or not
    if num <= 3:
        return False
    for i in range(4, ((num // 2) + 1)):
        if num % i == 0:
            return True
    return False


def sumdigits(num):
    # returns the sum of digits of a number
    listi = [int(n) for n in str(num)]
    return sum(listi)
