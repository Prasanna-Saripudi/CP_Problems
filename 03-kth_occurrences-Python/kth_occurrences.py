# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.
# author: Prasanna Saripudi


def fun_kth_occurrences(s, n):
    setStr = set(s)
    dict, counts = {}, []
    for x in setStr:
        c = s.count(x)
        counts.append(c)
        if c in dict.keys():
            dict[c].append(x)
        else:
            dict[c] = [x]
    counts.sort(reverse=True)
    freq = counts[n-1]
    return dict[freq][0]
