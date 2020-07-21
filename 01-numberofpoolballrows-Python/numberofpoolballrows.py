# Pool balls are arranged in balls where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row.
# numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, and returns the
# smallest int number of balls required for the given number of pool balls. Thus, numberOfPoolBallRows(6)
# returns 3. Note that if any balls must be in a row, then you count that row, and so
# numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single ball in it).
# author: Prasanna Saripudi
def fun_numberofpoolballrows(balls):
    if balls == 1:
        return 1
    count, val, sum = 1, 1, 1
    while True:
        count += 1
        if sum + val + 1 < balls:
            val += 1
            sum += val
        else:
            break
    return count
