"""
CodeAbbey, Problem 67
Coded by whoisrgj
"""

import math

T = int(input())

for tc in range(T):
    F = int(input())
    idx = round(math.log(F*math.sqrt(5)+0.5, (1+math.sqrt(5))/2))
    if idx < 0:
        print(0, end=' ')
    else:
        print(idx, end=' ')