# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).
# author: Prasanna Saripudi

def longestdigitrun(n):
    nStr = str(abs(n))
    start, end, max, i, count = 0, 0, 0, 0, 0
    while i < len(nStr):
        while nStr[start] == nStr[end]:
            end += 1
        if end - start > count:
            max = nStr[start]
        elif end - start == count:
            max = min(max, nStr[start])
        start, i = end, end
    return max
