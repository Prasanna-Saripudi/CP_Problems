# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that
# any values that would otherwise produce a consecutive run of k elements are not present.
# For example:
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3])
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3])
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on
# that copy and return it. Instead, you must directly construct the result here.
# author: Prasanna Saripudi

# deepcopy: copy.deepcopy(), using"=" ; modifies the list even after copy
# shallow copy: copy.copy(), listName.copy(),slicing ; wont be modified after copy


def shortenlongruns(L, k):
    copied = L.copy()
    start, end, i = 0, 0, 0
    while i < len(copied):
        while end < len(copied) and copied[start] == copied[end]:
            end += 1
        if end - start > k:
            index = (end - start) % k
            copied = copied[: start + index] + copied[end:]
            end = start+index
        elif end - start == k:
            copied = copied[: end - 1] + copied[end:]
            end -= 1
        start = end
        i = end
    return copied
