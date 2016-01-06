
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def combinations(n, k):
	return factorial(n) // (factorial(k) * factorial(n-k))
		
test_cases = int(input())
for i in range(test_cases):
	N, K = map(int, input().split())
	print(combinations(N, K), end=" ")
	