"""
CodeAbbey, Problem 45
Coded by Raul Gonzalez
"""


class Problem45:
    def __init__(self):
        self.RANKS = "A23456789TJQK"
        self.SUITS = "CDHS"
        self.deck = ["{}{}".format(s, r) for s in self.SUITS for r in self.RANKS]

    def solve(self):
        random_numbers = list(map(int, input().split()))
        for i in range(52):
            j = random_numbers[i] % 52
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        return " ".join(self.deck)


if __name__ == "__main__":

    print(Problem45().solve())
