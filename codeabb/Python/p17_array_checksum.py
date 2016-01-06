"""
CodeAbbey, Problem 17
Coded by whoisrgj
"""

N = int(input())
numbers = list(map(int, input().split()))
result = 0
for i in numbers:
    result += i
    result *= 113
    result %= 10000007
print(result)