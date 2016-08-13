"""
CodeAbbey, Problem 25
Coded by whoisrgj
"""


def lcg(a, c, m, x, n):
    for _ in range(n):
        x = (a * x + c) % m
    return x


def main():
    n = int(input())
    results = []
    for _ in range(n):
        results.append(lcg(*map(int, input().split())))
    print(*results)

if __name__ == '__main__':
    main()
