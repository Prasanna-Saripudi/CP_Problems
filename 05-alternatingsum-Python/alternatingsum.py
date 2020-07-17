# Write the function alternatingSum(a) that takes a list of numbers and returns the
# alternating sum (where the sign alternates from positive to negative or vice versa).
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.
# author: Prasanna Saripudi

def fun_alternatingsum(a):
    if len(a):
        result = 0
        for val in range(len(a)):
            result += a[val] if val % 2 == 0 else - a[val]
        return result
    return 0
