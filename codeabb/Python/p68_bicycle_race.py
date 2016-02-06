"""
CodeAbbey, Problem 68
Coded by whoisrgj
"""


def calculate(s, a, b):
    return (s/(a+b))*a


if __name__ == '__main__':
    N = int(input())
    print(" ".join(["{0:.8f}".format(calculate(*map(int, input().split()))) for _ in range(N)]))
