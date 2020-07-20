# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic
# square.
# author: Prasanna Saripudi

def fixmostlymagicsquare(L):
    le = len(L)
    rows = [sum(l) for l in L]
# cant intialize this way for mutable ones
    columns = [0] * le
    print(columns)
    for i in range(le):
        for j in range(le):
            columns[j] += L[i][j]
	# found the odd value and the has to be be sum value
    for j in rows:
        if rows.count(j) == 1:
            odd = j
        elif rows.count(j) > 1:
            val = j
    index1 = rows.index(odd)
    index2 = columns.index(odd)
	# replacing in positions
    L[index1][index2] -= odd-val
    return L
