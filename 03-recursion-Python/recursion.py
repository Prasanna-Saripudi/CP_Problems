"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""
# author: Prasanna Saripudi
# 0 1 1 2 3 5 8 13 21 34 55 89
# 0 1 2 3 4 5 6  7  8  9 10 11

def get_fib(position):
    if position==0:
        return 0
    elif position == 1:
        return 1
    s = get_fib(position - 1) + get_fib(position-2)
    return s
