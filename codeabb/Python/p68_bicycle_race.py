"""
CodeAbbey, Problem 68
Coded by whoisrgj
"""

N = int(input())
for tc in range(N):
    S,A,B = map(int, input().split())
    t = S/(A+B)
    print("{0:.8f}".format(t*A), end=' ')