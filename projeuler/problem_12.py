import math

def getDivisorCount(n):
    divisors = 0
    start = 1
    end = math.floor(math.sqrt(n))
    while start <= end:
        if n % start == 0:
            if start == n//start:
                divisors += 1
            else:
                divisors += 2
        start += 1
    return divisors

divisors = 0
inc = 0
triangle = 0
while divisors < 500:
    inc += 1
    triangle += inc
    divisors = getDivisorCount(triangle)
print(triangle)
    