# Write the function alternatingSum(L) that takes a possibly-empty list of numbers,
# and returns the alternating sum of the list, where every other value is subtracted
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.
# author: Prasanna Saripudi

def fun_recursions_alternatingsum(l):
    return rec_alternatingSum(l, 0, 0)


def rec_alternatingSum(listi, index, sum):
    if index == len(listi):
        return sum
    if index % 2 == 0:
        sum += listi[index]
        return rec_alternatingSum(listi, index + 1, sum)
    elif index % 2 != 0:
        sum -= listi[index]
        return rec_alternatingSum(listi, index+1, sum)
