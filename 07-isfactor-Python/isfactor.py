# Write the function isFactor(f, n) that takes
# two int values f and n, and returns True
# if f is a factor of n, and False otherwise.
# Note that every integer is a factor of 0.
# author: Prasanna Saripudi


def fun_isfactor(f, n):
    if f == 0 or n % f == 0 or n != 0:
        return True
    return False  # replace with your solution
