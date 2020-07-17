# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]
# author: Prasanna Saripudi
from collections import OrderedDict


def lookandsay(a):
    # can consider using ordered sets for having the sets in an order
    # from ordered_set import OrderedSet;os = OrderedSet(list)
    dict = OrderedDict()
    final = []
    for val in a:
        if val not in dict.keys():
            c = a.count(val)
            dict[val] = a.count(val)
    for key, value in dict.items():
        final.append((value, key))
    return final
