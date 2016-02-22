"""
CodeAbbey, Problem 128
Coded by whoisrgj
"""


def factorial(n):
    return n * factorial(n-1) if n > 0 else 1


def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))


def main():
    n = int(input())
    print(*(combinations(*map(int, input().split())) for _ in range(n)))

if __name__ == '__main__':
    main()
