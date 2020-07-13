# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.
#author: Prasanna Saripudi

def isevenpositiveint(x):
	# checking type, positive, even
	if type(x) is int and x >0 and x%2==0:
		return True
	return False
