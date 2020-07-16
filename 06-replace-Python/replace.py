# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().
# author: Prasanna Saripudi


def fun_replace(s1, s2, s3):
    for i in range(len(s1) - len(s2)):
        if s1[i: i + len(s2)] == s2:
            print(s1[i: i + len(s2)], s2)
            return s1[:i]+s3+s1[i+len(s2):]
    return s1
