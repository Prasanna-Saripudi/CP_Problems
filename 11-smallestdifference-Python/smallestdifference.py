# Write the function smallestDifference(a) that takes a list of integers and returns
# the smallest absolute difference between any two
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.
# author: Prasanna Saripudi

def smallestdifference(a):
    if len(a) == 0:
        return -1
    diff = 10 ** 20
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            calc = abs(a[i] - a[j])
            if calc < diff:
                diff = calc
    return diff
