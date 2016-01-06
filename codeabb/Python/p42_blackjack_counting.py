"""
CodeAbbey, Problem 42
Coded by whoisrgj
"""

high_cards = set('TJQK')
 
N = int(input())
for i in range(N):
    cards = list(input().split())
    pts = 0
    aces = 0
    for card in cards:
        if card == 'A':
            if pts < 12:
                pts += 11
                aces += 1
            else:
                pts += 1
        elif card in high_cards:
            pts += 10
        else:
            pts += int(card)
        if pts > 21 and aces > 0:
            pts -= 10
            aces -= 1
    if pts > 21:
        print("Bust", end= ' ')
    else:
        print(pts, end=' ')