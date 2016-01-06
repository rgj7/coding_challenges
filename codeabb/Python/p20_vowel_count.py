"""
CodeAbbey, Problem 20
Coded by whoisrgj
"""

N = int(input())
vowels = set('aeiouy')
for i in range(N):
    count = 0
    line = input()
    for c in line:
        if c in vowels:
            count += 1 
    print(count, end=' ')