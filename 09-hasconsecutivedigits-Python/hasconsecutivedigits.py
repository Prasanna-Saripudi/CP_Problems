# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that
# number contains two consecutive digits that are the same, and False otherwise.
# author: Prasanna Saripudi

def hasconsecutivedigits(n):
    n = abs(n)
    # st = str(n)
    # for x in range(len(st)-1):
    #     if st[x] == st[x + 1]:
    #         return True
    # return False
    temp = n
    while temp > 0:
        rem = temp % 10
        temp //= 10
        if rem == temp % 10:
            return True
    return False
