"""
CodeAbbey, Problem 32
Coded by whoisrgj
"""

N, K = map(int, input().split())
numbers = list(range(1, N+1))

offset = 0
while len(numbers) > 1:
    offset = len(numbers)+offset % K
    del numbers[K-1-offset::K]
print(numbers[0])