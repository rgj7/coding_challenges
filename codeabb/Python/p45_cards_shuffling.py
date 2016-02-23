"""
CodeAbbey, Problem 45
Coded by Raul Gonzalez
"""

RANKS = "A23456789TJQK"
SUITS = "CDHS"


def cards_shuffling(random_numbers):
    deck = ["{}{}".format(s, r) for s in SUITS for r in RANKS]
    for i in range(len(random_numbers)):
        j = random_numbers[i] % len(random_numbers)
        deck[i], deck[j] = deck[j], deck[i]
    return deck


def main():
    rand_values = list(map(int, input().split()))
    print(" ".join(cards_shuffling(rand_values)))

if __name__ == "__main__":
    main()
