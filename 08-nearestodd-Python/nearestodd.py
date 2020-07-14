# Write the function nearestOdd(n) that takes an float n,
# and returns as an int value the nearest odd number to n.
# In the case of a tie, return the smaller odd value.
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.
# author: Prasanna Saripudi


def fun_nearestodd(n):
    temp = str(n).split(".")
    # getting deigit and decimal both
    digit = int(temp[0])
    deci = int(temp[1])
    # if digit odd, nearest odd is itself
    if digit % 2 != 0:
        return digit
    # if digit even, then only if tie smallest odd, otherwise largest odd
    if (deci == 0):
        return digit - 1
    return digit + 1
