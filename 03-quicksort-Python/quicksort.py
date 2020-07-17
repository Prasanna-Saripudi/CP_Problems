"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
# author: Prasanna Saripudi


def quicksort(array):
    quicksort(array, 0, len(array))
    return array

# recursive function continues until sorted


def quicksort(array, low, high):
    if low < high:
        parted = partition(array, low, high)
        quicksort(array, low, parted - 1)
        quicksort(array, parted+1, high)

# parts the array based on pivot and returns the parted value


def partition(array, low, high):
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
    array[low], array[end] = array[end], array[start]
    return end
