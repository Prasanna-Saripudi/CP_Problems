# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.
# author: Prasanna Saripudi

def fun_recursion_onlyevendigits(l):
    return rec_onlyEven(l, 0)


def rec_onlyEven(listi, index):
    if index == len(listi):
        return listi
    temp, position, temp1 = listi[index], 0, 0
    while temp > 0:
        d = temp % 10
        if d % 2 == 0:
            temp1 += d * (10 ** position)
            position += 1
            print(temp1)
        temp = temp // 10
    listi[index] = temp1
    return rec_onlyEven(listi, index+1)
