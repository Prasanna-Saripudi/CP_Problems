# Write the function getKthDigit(n, k) that takes
# a possibly-negative int n and a non-negative int k,
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0
# author: Prasanna Saripudi

def fun_get_kth_digit(digit, k):
    digit = str(abs(digit))
    if k >= len(digit):
        return 0
    return int(digit[len(digit)-1-k])
