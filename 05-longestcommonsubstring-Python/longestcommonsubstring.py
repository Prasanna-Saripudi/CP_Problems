# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"
# author: Prasanna Saripudi

def longestcommonsubstring(s1, s2):
    if s1 == "" or s2 == "":
        return ""
    commons, maxi = [], 0
    minStr, maxStr = min(s1, s2), max(s1, s2)
    for i in range(len(minStr)):
        j = len(minStr)-1
        while j >= 1:
            # print(minStr[i:j])
            x = minStr[i:j+1]
            if x in maxStr and len(x) > maxi:
                commons.append(x)
                maxi = len(x)
                print(commons)
            j -= 1
    commons.sort()
    return commons[0]
