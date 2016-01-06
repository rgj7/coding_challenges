"""
CodeAbbey, Problem 39
Coded by Raul Gonzalez
"""

import math


class Problem39:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices

    def solve(self):
        mean = sum(self.prices)/len(self.prices)
        std_dev = math.sqrt(sum([(mean-price)**2 for price in self.prices])/len(self.prices))
        return True if std_dev >= mean*0.04 else False


def get_input():
    line = input().split()
    name = line.pop(0)
    prices = list(map(int, line))
    return name, prices

if __name__ == "__main__":
    valid_stocks = list()
    num_test_cases = int(input())
    for test_case in range(num_test_cases):
        stock_name, stock_prices = get_input()
        problem = Problem39(stock_name, stock_prices)
        if problem.solve():
            valid_stocks.append(stock_name)
    print(" ".join(valid_stocks))
