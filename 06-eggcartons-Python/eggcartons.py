# Write the function eggCartons(eggs) that takes
# a non-negative integer number of eggs, and returns
# the smallest integer number of cartons required to hold
# that many eggs, where a carton may hold up to 12 eggs
# author: Prasanna Saripudi

def fun_eggcartons(eggs):
    # cartons needed for total eggs
    cartons = eggs // 12
    # checking for rem eggs
    if (eggs % 12) > 0:
        cartons += 1
    return cartons
