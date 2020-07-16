"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
# author: Prasanna Saripudi

# in python can directly do that by checking if its there and fetching the index of that elemnt
# binary search, is by comparing the search element with mid and cotinues


def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low+high)//2
        if value > input_array[mid]:
            low = mid + 1
        elif value < input_array[mid]:
            high = mid - 1
        else:
            return mid
    return -1
