"""
CodeAbbey, Problem 49
Coded by whoisrgj
"""


def solve(list_of_games):
    player1, player2 = 0, 0
    for game in list_of_games:
        if game in ('RS', 'SP', 'PR'):
            player1 += 1
        elif game in ('SR', 'PS', 'RP'):
            player2 += 1
    return 1 if player1 > player2 else 2


def main():
    n = int(input())
    print(*(solve(input().split()) for _ in range(n)))

if __name__ == '__main__':
    main()
