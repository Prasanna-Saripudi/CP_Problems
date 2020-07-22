# Write the function sumOfSquaresOfDigits(n) which takes a non-negative integer and returns the
# sum of the squares of its digits. Here are some test assertions for you:
# assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
# assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
# assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29
# author: Prasanna Saripudi

def sumofsquaresofdigit(n):
    # return sum(int(x)**2 for x in str(n))
    sum = 0
    while n > 0:
        d = n % 10
        sum += d ** 2
        n //= 10
    return sum
