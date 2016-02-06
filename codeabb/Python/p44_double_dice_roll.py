"""
CodeAbbey, Problem 44
Coded by whoisrgj
"""


def calculate(a, b):
    return ((a % 6) + 1) + ((b % 6) + 1)

if __name__ == '__main__':
    N = int(input())
    print(*map(str, [calculate(*map(int, input().split())) for _ in range(N)]))
