"""
CodeAbbey, Problem 35
Coded by whoisrgj
"""

N = int(input())

for tc in range(N):
    S, R, P = map(int, input().split())
    year = 0
    money = S
    P /= 100
    while money < R:
        money += money*P
        money = float("%.3f" % money)
        print(money)
        year += 1
    print(year, end=' ')