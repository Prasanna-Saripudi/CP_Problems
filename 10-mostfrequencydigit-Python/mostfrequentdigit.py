# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.
# author: Prasanna Saripudi

def mostfrequentdigit(n):
    n = str(n)
    maxfreqCount = 0
    maxFreq = 0
    for x in n:
        if n.count(x) > maxfreqCount:
            maxFreq = int(x)
            maxfreqCount += 1
        if n.count(x) == maxfreqCount:
            maxFreq = min(maxFreq, int(x))
    return maxFreq
