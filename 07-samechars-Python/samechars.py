# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either
# parameter is not a string, but returns True if both strings are empty (why?).
# author: Prasanna Saripudi

def samechars(s):
    s1, s2 = s[0], s[1]
    if s1 == s2:
        return True
    if type(s1) == type(s2):
        x, y = sorted(list(set(s1))), sorted(list(set(s2)))
        if len(x) == len(y) and x == y:
            return True
    return False
