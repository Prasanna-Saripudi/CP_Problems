# Write the function smallestDifference(a) that takes a list of integers and returns
# the smallest absolute difference between any two
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.
# author: Prasanna Saripudi

# for o(nlogn)=> can sort initially with o(logn) and then with o(n) compare the sorted consec for min diff
# o(n^2) would be to iterate using 2 loops

def smallestdifference(a):
    if len(a) == 0:
        return -1
    diff = 10 ** 20
    a.sort()
    for x in range(len(a) - 1):
        if abs(a[x + 1] - a[x]) < diff:
            diff = abs(a[x + 1] - a[x])
    return diff
    # for i in range(len(a)-1):
    #     for j in range(i+1, len(a)):
    #         calc = abs(a[i] - a[j])
    #         if calc < diff:
    #             diff = calc
    # return diff
