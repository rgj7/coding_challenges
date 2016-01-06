"""
CodeAbbey, Problem 94
Coded by whoisrgj
"""

N = int(input())
for i in range(N):
    numbers = list(map(int, input().split()))
    print(sum([x**2 for x in numbers]), end= ' ')