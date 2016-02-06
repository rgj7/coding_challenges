"""
CodeAbbey, Problem 42
Coded by whoisrgj
"""

FACE_CARDS = frozenset('TJQK')


def blackjack_result(cards):
    points, ace_count = 0, 0
    for card in cards:
        if card == 'A':
            points += 11
            ace_count += 1
        elif card in FACE_CARDS:
            points += 10
        else:
            points += int(card)
    while points > 21 and ace_count > 0:
        points -= 10
        ace_count -= 1
    return "Bust" if points > 21 else str(points)


if __name__ == '__main__':
    N = int(input())
    print(" ".join([blackjack_result(list(input().split())) for _ in range(N)]))