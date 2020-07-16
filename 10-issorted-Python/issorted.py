# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list
# is sorted (either smallest-first or largest-first) and False otherwise. Your function
# must only consider each value in the list once (so, in terms of big-oh, which we will
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort
# the list.
# author: Prasanna Saripudi

def issorted(a):
    if len(a) in [0, 1]:
        return True
    if a[0] >= a[1]:
        flag = True
    else:
        flag = False
    val = a[0]
    for i in a[1:]:
        if (flag and val >= i) or (not flag and val <= i):
            val = i
        else:
            return False
    return True
