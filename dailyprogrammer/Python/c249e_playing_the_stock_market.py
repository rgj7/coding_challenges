"""
r/DailyProgrammer
Challenge 249, Easy
Solution by whoisrgj
"""


class Challenge249E:
    def __init__(self, quotes):
        self.quotes = quotes

    def solve(self):
        max_profit, buy, sell = 0, 0, 0
        for index, q1 in enumerate(self.quotes[:-2], 0):
            for q2 in self.quotes[index+2:]:
                if q2-q1 > max_profit:
                    max_profit, buy, sell = q2-q1, q1, q2
        print(buy, sell)

if __name__ == '__main__':
    Challenge249E(list(map(float, input().split()))).solve()
