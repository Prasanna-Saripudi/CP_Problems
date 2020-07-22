# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!
# author: Prasanna Saripudi

def ishappyprimenumber(n):
    if isHappy(n) and isPrime(n):
        return True
    return False


def isHappy(num):
    visited = set()
    while num != 1:
        num = sum(int(x) ** 2 for x in str(num))
        if num in visited:
            return False
        visited.add(num)
    return True


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, ((num // 2) + 1)):
        if num % i == 0:
            return False
    return True
