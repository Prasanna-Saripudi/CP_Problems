# Write the function interleave(s1, s2) that takes two strings, s1 and s2,
# and interleaves their characters starting with the first character in s1.
# For example, interleave('pto', 'yhn') would return the string "python".
# If one string is longer than the other, concatenate the rest of the remaining
# string onto the end of the new string. For example ('a#', 'cD!f2') would return
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.
# author: Prasanna Saripudi


def fun_interleave(s1, s2):
    minStr, maxStr = s1, s2
    if len(s2) < len(s1):
        minStr, maxStr = s2, s1
    result = []
    i = 0
    for i in range(len(minStr)):
        result.append(s1[i] + s2[i])
    result.append(maxStr[i+1:])
    return "".join(result)
