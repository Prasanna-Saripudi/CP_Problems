# Write the function pascalsTriangleValue(row, col)
# that takes int values row and col, and returns the
# value in the given row and column of Pascal's
# Triangle where the triangle starts at row 0, and
# each row starts at column 0. If either row or col
# are not legal values, return None, instead of crashing.
# author: Prasanna Saripudi


# formula of the coeff value [n!/(k!*(n-k)!)] n, k are row, culumns in pascal
def fun_pascaltrianglevalue(row, col):
    if col > row:
        return 0
    elif row == col or col == 0:
        return 1
    coeff = fact(row) // (fact(col)*fact(row-col))
    return coeff


def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)
