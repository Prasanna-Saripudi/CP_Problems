# Write the function isMultiple that takes two int values m and n
# and returns True if m is a multiple of n and False otherwise.
# Note that 0 is a multiple of every integer including itself.
# Also, you should make constructive use of the isFactor function you just wrote above.
# author: Prasanna Saripudi


def fun_ismultiple(m, n):
    # 7 * 2 = 14 ; 7, 2 are factors of 14; 14 is a multiple of 7, 2
    if n == 0 and m != 0:
        return False
    elif m == 0 or m % n == 0:
        return True
    return False
