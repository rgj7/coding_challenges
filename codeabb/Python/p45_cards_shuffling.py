"""
CodeAbbey, Problem 45
Coded by Raul Gonzalez
"""

RANKS = "A23456789TJQK"
SUITS = "CDHS"


def solve(random_numbers):
    deck = ["{}{}".format(s, r) for s in SUITS for r in RANKS]
    for i in range(52):
        j = random_numbers[i] % 52
        deck[i], deck[j] = deck[j], deck[i]
    return deck

if __name__ == "__main__":
    print(*solve(list(map(int, input().split()))))
