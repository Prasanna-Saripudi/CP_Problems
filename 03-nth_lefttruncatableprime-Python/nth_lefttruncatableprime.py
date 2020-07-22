# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.
# author: Prasanna Saripudi

def fun_nth_lefttruncatableprime(n):
    count, value = 0, 2
    while count < n:
        value += 1
        if isLeftTruncPrime(value):
            count += 1
    return value


def isLeftTruncPrime(num):
    numStr = str(num)[::-1]
    # checking if 0 in number
    if '0' in numStr:
        return False
    # checking if the truncated numbers are primes
    for i in range(len(numStr)):
        x = int(numStr[: i + 1][::-1])
        # if not prime, then False
        if not isPrime(x):
            return False
    return True


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, ((num // 2) + 1)):
        if num % i == 0:
            return False
    return True
