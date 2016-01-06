def fibo_div(m):
	if m == 1:
		return 1
	a = 1
	b = 1
	c = 2
	idx = 3
	while c % m > 0:
		a = b
		b = c
		c = a+b
		idx += 1
	return idx

""" begin """	

test_cases = int(input())
divisors = list(map(int, input().split()))

for tc in range(test_cases):
	print(fibo_div(divisors[tc]), end=" ")