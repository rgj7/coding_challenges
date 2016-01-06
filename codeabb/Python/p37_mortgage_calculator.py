"""
CodeAbbey, Problem 37
Coded by Raul Gonzalez
"""

import math


class Problem37:
    def __init__(self, p, i, m):
        self.principle = p
        self.yearly_interest = i
        self.months = m

    def solve(self):
        monthly_interest = self.yearly_interest/1200
        x = (1+monthly_interest)**self.months
        monthly_payment = self.principle*((monthly_interest*x)/(x-1))
        return math.ceil(monthly_payment)


if __name__ == "__main__":
    P, I, M = map(int, input().split())
    print(Problem37(P, I, M).solve())
