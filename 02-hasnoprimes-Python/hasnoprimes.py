# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.
# author: Prasanna Saripudi

def fun_hasnoprimes(l):
    for listi in l:
        for ele in listi:
            if isPrime(ele):
                return False
    return True


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, ((num // 2) + 1)):
        if num % i == 0:
            return False
    return True
