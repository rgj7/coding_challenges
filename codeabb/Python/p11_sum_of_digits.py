"""
CodeAbbey, Problem 11
Coded by whoisrgj
"""

N = int(input())
for i in range(N):
    num1, num2, num3 = map(int, input().split())
    result = (num1*num2)+num3;
    print(sum(map(int, str(result))), end=' ')
    