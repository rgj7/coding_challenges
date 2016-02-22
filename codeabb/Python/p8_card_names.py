"""
CodeAbbey, Problem 8
Coded by whoisrgj
"""

SUITS = "Clubs Spades Diamonds Hearts".split()
RANKS = "2 3 4 5 6 7 8 9 10 Jack Queen King Ace".split()


def get_card_name(value):
    return "{}-of-{}".format(RANKS[value % 13], SUITS[value // 13])


def main():
    n = int(input())
    card_values = map(int, input().split())
    print(" ".join([get_card_name(val) for val in card_values]))

if __name__ == '__main__':
    main()
