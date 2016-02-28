"""
CodeAbbey, Problem 80
Coded by whoisrgj
"""


def duel_chances(a, b):
    a_miss = 1 - (a / 100)
    b_miss = 1 - (b / 100)
    return round(a / (1 - (a_miss * b_miss)))


def main():
    n = int(input())
    print(*[duel_chances(a, b) for a, b in (map(int, input().split()) for _ in range(n))])

if __name__ == '__main__':
    main()
