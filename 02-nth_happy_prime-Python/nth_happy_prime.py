# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).
# author: Prasanna Saripudi


def fun_nth_happy_prime(n):
    count = 0
    num = 1
    while count <= n:
        num += 1
        if isHappy(num) and isPrime(num):
            count += 1
    return num


def isHappy(num):
    visited = set()
    while num != 1:
        num = sum(int(x) ** 2 for x in str(num))
        if num in visited:
            return False
        visited.add(num)
    return True


def isPrime(num):
    for i in range(2, (num // 2)+1):
        if i % 2 == 0:
            return False
    return True
