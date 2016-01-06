"""
CodeAbbey, Problem 47
Coded by whoisrgj
"""

import string
N, K = map(int, input().split())
letters = list(string.ascii_uppercase)
for i in range(N):
    line = input()
    for c in line:
        index = ord(c)
        print(letters[(index-65-K)%26] if 64<index<91 else c, end='')
    print('', end=' ')
