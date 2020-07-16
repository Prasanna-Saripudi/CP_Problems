# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().
# author: Prasanna Saripudi


def fun_replace(s1, s2, s3):
    freq = s1.count(s2)
    if freq == 0:
        return s1
    elif freq == 1:
        index = s1.index(s2)
        return s1[:index] + s3 + s1[index + len(s2):]
    indexes = [i for i in range(len(s1) - len(s2) + 1) if s1.startswith(s2, i)]
    j = indexes[0]
    for i in indexes[1:]:
        s1 = s1[:j] + s3 + s1[j + len(s2):]
        j += i
    return s1
# for i in range(len(s1) - len(s2)+1):
#     print(s1[i: i + len(s2)], s2)
#     if s1[i: i + len(s2)] == s2:
#         return s1[:i]+s3+s1[i+len(s2):]
# return s1
