# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.
# author: Prasanna Saripudi

def fun_carrylessadd(x, y):
    xStr, yStr = str(x)[::-1], str(y)[::-1]
    minStr, maxStr = min(xStr, yStr), max(xStr, yStr)
    result = ''
    for i in range(len(minStr)):
        result += str(int(minStr[i]) + int(maxStr[i]))[-1]
    if i < len(maxStr):
        result += maxStr[i+1:]
    return int(result[::-1])
