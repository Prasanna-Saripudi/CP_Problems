"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
# author: Prasanna Saripudi


def quicksort(array):
    quicksort1(array, 0, len(array)-1)
    return array


def quicksort1(array, low, high):
    # recursive function continues until sorted
    if low < high:
        parted = partition(array, low, high)
        quicksort1(array, low, parted - 1)
        quicksort1(array, parted+1, high)


def partition(array, low, high):
    # parts the array based on pivot and returns the parted value
    # taking first elemnt as pivot
    pivot = array[low]
    start = low + 1
    end = high
    while True:
        while start <= end and array[start] <= pivot:
            start += 1
        while start <= end and array[end] >= pivot:
            end -= 1
        if start <= end:
            array[start], array[end] = array[end], array[start]
        else:
            break
    array[low], array[end] = array[end], array[low]
    return end
