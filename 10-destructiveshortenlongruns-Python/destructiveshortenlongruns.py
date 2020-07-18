# Here we will rewrite the previous function to be destructive. This version must not just call the nondestructive
# version from above and then clear and replace the values in the original list. Instead, you must traverse the list
# once and make the changes to the list as you go. With that in mind, write the destructive function shortenLongRuns(
# L, k) that takes a list L and a positive integer k, and destructively modifies L by removing any values in L that
# would otherwise produce a run of k consecutive equal values in L.
# For example:
# L = [2, 3, 5, 5, 5, 3]
# shortenLongRuns(L, 2)
# assert(L == [2, 3, 5, 3])
# And:
# L = [2, 3, 5, 5, 5, 3]
# shortenLongRuns(L, 3)
# assert(L == [2, 3, 5, 5, 3])
# author: Prasanna Saripudi

def destructiveshortenlongruns(L, k):
    start, end, i = 0, 0, 0
    while i < len(L):
        while end < len(L) and L[start] == L[end]:
            end += 1
        if end - start > k:
            index = (end - start) % k
            if index == 0:
                index = k - 1
            L = L[: start + index] + L[end:]
            end = start + index
        elif end - start == k:
            L = L[: end - 1] + L[end:]
            end -= 1
        start = end
        i = end
    return L
