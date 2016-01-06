import math

def getPrimeFactors(n):
	prime_factors = list()
	remainder = n
	prod = 1
	sqmax = int(math.sqrt(n))
	i = 2
	while(remainder > 0 and i <= sqmax):
		if remainder % i == 0:
			prime_factors.append(str(i))
			remainder //= i
			prod *= i
			continue
		i += 1
	if prod < n:
		prime_factors.append(str(n//prod))
	return prime_factors
	
""" begin """

test_cases = int(input())

for i in range(test_cases):
	val = int(input())
	print("*".join(getPrimeFactors(val)), end=" ")

