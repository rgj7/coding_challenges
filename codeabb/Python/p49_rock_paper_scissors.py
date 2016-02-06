"""
CodeAbbey, Problem 49
Coded by whoisrgj
"""


def solve(games):
    player1, player2 = 0, 0
    for game in games:
        if game in ('RS', 'SP', 'PR'):
            player1 += 1
        elif game in ('SR', 'PS', 'RP'):
            player2 += 1
    return 1 if player1 > player2 else 2

if __name__ == '__main__':
    N = int(input())
    print(*[solve(list(input().split())) for _ in range(N)])
