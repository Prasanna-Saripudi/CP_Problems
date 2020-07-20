# Write the function matrixMultiply(m1, m2) that takes two 2d lists
# (that we will consider to be matrices) and returns a new 2d list that
# is the result of multiplying the two matrices. Return None if the
# two matrices cannot be multiplied for any reason.
# author: Prasanna saripudi

def fun_matrixmultiply(m1, m2):
    r1, c1 = len(m1), len(m1[0])
    r2, c2 = len(m2), len(m2[0])
    if c1 != r2:
        return None
    # can directly multiply by using numpy dot
    # now working based on iterations
    result = [[0] * c2 for i in range(r1)]
    # rows of m1
    for i in range(r1):
        # columns of m2
        for j in range(c2):
            # rows of m2
            for k in range(r2):
                result[i][j] += m1[i][k] + m2[k][j]
    return result
