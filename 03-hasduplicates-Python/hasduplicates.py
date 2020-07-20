# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L
# contains any duplicate values (that is,
# if any two values in L are equal to each other), and False otherwise.
# author: Prasanna Saripudi

def hasduplicates(L):
    # for flattening 2d to 1d list
    listi = sum(L, [])
    # checking the 1d list length and the set length for duplicates
    if len(listi) > len(set(listi)):
        return True
    return False
