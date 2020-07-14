# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative
# single digit (between 0 and 9 inclusive). This function returns the number n with
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left,
# so the 0th digit is the rightmost digit.
# author: Prasanna Saripudi


def fun_set_kth_digit(n, k, d):
    flag = True
    if n < 0:
        flag = False
    n = abs(n)
    if k >= len(str(n)):
        n += d * (10 ** k)
    elif k < len(str(n)) and k >= 0:
        temp = str(n)
        temp = temp[:len(temp)-1-k] + str(d)+temp[len(temp)-k:]
        n = int(temp)
    if not flag:
        n = -n
    return n
