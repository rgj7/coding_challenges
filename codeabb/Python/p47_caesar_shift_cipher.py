"""
CodeAbbey, Problem 47
Coded by whoisrgj
"""

import string


def csc(ch, k):
    try:
        return string.ascii_uppercase[string.ascii_uppercase.index(ch)-k]
    except ValueError:
        return ch


def main():
    n, k = map(int, input().split())
    results = list()
    for _ in range(n):
        line = input()
        results.append("".join([csc(c, k) for c in line]))
    print(" ".join(results))

if __name__ == '__main__':
    main()
