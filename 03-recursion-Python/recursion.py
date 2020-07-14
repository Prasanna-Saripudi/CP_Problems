"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""
# author: Prasanna Saripudi
# 0 1 2 3 5 8 13 21 34


def get_fib(position):
    if position in [0, 1]:
        return 0
    elif position == 2:
        return 1
    else:
        x = get_fib(position - 1)
        y = get_fib(position-2)
        s = x + y
        print(x, y)
        print(position - 1, position-2, s)
        return s
