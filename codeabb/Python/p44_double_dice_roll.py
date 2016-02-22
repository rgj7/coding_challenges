"""
CodeAbbey, Problem 44
Coded by whoisrgj
"""


def calculate(a, b):
    return ((a % 6) + 1) + ((b % 6) + 1)


def main():
    n = int(input())
    print(*(calculate(*map(int, input().split())) for _ in range(n)))

if __name__ == '__main__':
    main()
