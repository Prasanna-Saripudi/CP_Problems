# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
# author: Prasanna Saripudi

def fun_nth_additive_prime(n):
    count = -1
    num = 2
    while n > count:
        sumofN = sum([int(x) for x in str(num)])
        if isPrime(num) and isPrime(sumofN):
            count += 1
        if count == n:
            return num
        num += 1


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True
