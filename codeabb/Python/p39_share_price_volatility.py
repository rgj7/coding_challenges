"""
CodeAbbey, Problem 39
Coded by Raul Gonzalez
"""

import math


def is_valid_stock(stock_quotes):
    mean = sum(stock_quotes)/len(stock_quotes)
    std_dev = math.sqrt(sum([(mean-price)**2 for price in stock_quotes])/len(stock_quotes))
    return True if std_dev >= mean*0.04 else False


def parse_line():
    line = input().split()
    stock_name = line[0]
    stock_quotes = list(map(int, line[1:]))
    return stock_name, stock_quotes


if __name__ == "__main__":
    N = int(input())
    data = [parse_line() for _ in range(N)]
    valid_stocks = [stock_name for stock_name, stock_quotes in data if is_valid_stock(stock_quotes)]
    print(*valid_stocks)
