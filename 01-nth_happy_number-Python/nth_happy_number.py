# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)
# author: Prasanna Saripudi

def fun_nth_happy_number(n):
    count = 0
    num = 0
    while count <= n:
        num += 1
        if (isHappy(num)):
            count += 1
    return num


def isHappy(num):
    # if the sum value repeats , then it isnt happy number
    visited = set()
    while num != 1:
        num = sum(int(x) ** 2 for x in str(num))
        if num in visited:
            return False
        visited.add(num)
    return True
