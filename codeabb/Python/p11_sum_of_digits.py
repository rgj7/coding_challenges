"""
CodeAbbey, Problem 11
Coded by whoisrgj
"""


def sum_of_digits(number):
    return sum([int(ch) for ch in str(number)])

if __name__ == '__main__':
    N = int(input())
    results = list()
    for _ in range(N):
        a, b, c = map(int, input().split())
        results.append(str(sum_of_digits((a*b)+c)))
    print(" ".join(results))
