# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().
# author: Prasanna Saripudi


def fun_replace(s1, s2, s3):
    freq = s1.count(s2)
    # returning the s1 if no matches
    if freq == 0:
        return s1
        # if matches, finding the indexes of matches
    indexes = [i for i in range(len(s1) - len(s2) + 1) if s1.startswith(s2, i)]
    j = indexes[0]
    # replacing s3 in s1 for all matches of s2
    for i in range(len(indexes)):
        s1 = s1[:j] + s3 + s1[j + len(s2):]
        if i == len(indexes)-1:
            break
        j = indexes[i + 1] + len(s3) - len(s2)
    return s1
