# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.
# author: Prasanna Saripudi

def fun_nearestkaprekarnumber(n):
    dec_n, inc_n = n, n
    while True:
        dec_n -= 1
        inc_n += 1
        if isKaprekar(dec_n) and isKaprekar(inc_n):
            return min(dec_n, inc_n)
        elif isKaprekar(dec_n):
            return dec_n
        elif isKaprekar(inc_n):
            return inc_n


def isKaprekar(num):
    sqr = num ** 2
    sqr_digits, split_digits = len(str(sqr)), 0
    while split_digits < sqr_digits:
        split_digits += 1
        split_val = 10 ** split_digits
        if split_val == num:
            continue
        sum = int(sqr / split_val) + (sqr % split_val)
        if sum == num:
            return True
    return False
