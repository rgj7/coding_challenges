"""
CodeAbbey, Problem 44
Coded by whoisrgj
"""

N = int(input())
for tc in range(N):
    A, B = map(int, input().split())
    print(((A % 6)+1) + ((B % 6)+1), end=' ')