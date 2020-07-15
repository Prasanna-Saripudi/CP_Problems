# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.
#author: Prasanna Saripudi
import math

def largestperfectsquare(n):
	root = math.sqrt(n)
	# checking if n is perfect square
	if root ** 2 == n and '0' == str(root).split('.')[1]:
		return n
	# else finding the below largest perfect square
	return int(str(root).split(".")[0])**2