"""
CodeAbbey, Problem 49
Coded by whoisrgj
"""

N = int(input())

for i in range(N):
    rounds = list(input().split())
    player1, player2 = 0, 0
    for round in rounds:
        if round in ('RS', 'SP', 'PR'):
            player1 += 1
        elif round in ('SR', 'PS', 'RP'):
            player2 += 1
    print(1 if player1 > player2 else 2, end=' ')