"""
CodeAbbey, Problem 42
Coded by whoisrgj
"""


def blackjack_result(cards):
    """
    Determines the result of a Blackjack game, given a list of cards.
    :param cards: A list of card values.
    :return: A string with the result.
    """
    points, ace_count = 0, 0
    for card in cards:
        if card == 'A':
            points += 11
            ace_count += 1
        elif card in 'TJQK':
            points += 10
        else:
            points += int(card)
    while points > 21 and ace_count > 0:
        points -= 10
        ace_count -= 1
    return "Bust" if points > 21 else str(points)


def main():
    n = int(input())
    print(*(blackjack_result(input().split()) for _ in range(n)))

if __name__ == '__main__':
    main()
