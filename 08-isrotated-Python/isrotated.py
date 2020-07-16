# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.
# author: Prasanna Saripudi

def isrotated(str1, str2):
    val = 0
    while val < len(str1):
        if str1[val:] + str1[:val] == str2 or str1[len(str1)-val:]+str1[:len(str1)-val] == str2:
            return True
        val += 1
    return False
