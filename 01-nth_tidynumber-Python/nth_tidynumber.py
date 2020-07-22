# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
# author: Prasanna Saripudi
def fun_nth_tidynumber(n):
    count, value = 0, 1
    while count < n:
        value += 1
        if isTidy(value):
            count += 1
    return value


def isTidy(num):
    numStr = str(num)
    for i in range(len(numStr) - 1):
        if int(numStr[i]) > int(numStr[i + 1]):
            return False
    return True
