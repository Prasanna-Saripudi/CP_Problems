# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.
# author: Prasanna Saripudi

def nthwithproperty309(n):
    count, value = 0, 309
    checkList = list("0123456789")
    while count < n:
        value += 1
        powOf5 = value ** 5
        list1 = list(str(powOf5))
        if set(checkList).issubset(set(list1)):
            count += 1
    return value
