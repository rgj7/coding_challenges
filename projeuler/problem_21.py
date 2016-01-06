import math

amicable = []

def getDivisors(n):
    divisors = [1]
    start = 2
    end = math.floor(math.sqrt(n))
    while start <= end:
        if n % start == 0:
            d = n//start
            if start == d:
                divisors.append(start)
            else:
                divisors.append(start)
                divisors.append(d)
        start += 1
    return divisors

for i in range(1,10000):
    r1 = sum(getDivisors(i))
    r2 = sum(getDivisors(r1))
    if i == r2:
        amicable.append(i)
        amicable.append(r1)
        
print(sum(amicable))