# islegaltriangle(s1, s2, s3)
# Write the function islegaltriangle(s1, s2, s3) that takes three int or float values representing
# the lengths of the sides of a triangle, and returns True if such a triangle exists and False
# otherwise. Note from the triangle inequality that the sum of each two sides must be greater
# than the third side, and further note that all sides of a legal triangle must be positive. Hint:
# how can you determine the longest side, and how might that help?
# author: Prasanna Saripudi

def islegaltriangle(s1, s2, s3):
    sides = [s1, s2, s3]
    maxSideInd = sides.index(max(sides))
    remSides = [i for i in [0, 1, 2] if i != maxSideInd]
	# checking if largestside is lessthanthesumofrem2sides; TRUE
    if sides[remSides[0]] + sides[remSides[1]] > sides[maxSideInd]:
        return True
    return False
