# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.
# author: Prasanna Saripudi
# from collections import OrderedDict


def removeduplicate(text):
    # return "".join(OrderedDict.fromkeys(text))
    result = ""
    for c in text:
        if c in result:
            pass
        else:
            result += c
    return result
