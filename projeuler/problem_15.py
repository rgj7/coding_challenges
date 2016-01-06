import math

def C(n,k):
    return math.factorial(n)//(math.factorial(n-k)*math.factorial(k))

# I can go only down or right.
# 20x20 grid = 40 possible moves in one navigation run.
# Maximum 20 for each R or D, otherwise I'll go out of bounds.
# Out of 40 total moves, how many unique combinations can I have with 20 R and 20 D?
# answer 40! / 20!*20!
# 40! = total possible combinations
# remove redundancies by dividing 20!*20!

print(C(40,20))