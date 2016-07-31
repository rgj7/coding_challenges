"""
CodeAbbey, Problem 39
Coded by whosirgj
"""
from collections import namedtuple

Stock = namedtuple('Stock', 'name quotes')


def is_stock_valid(quotes):
    mean = sum(quotes)/len(quotes)
    quad_distance = sum((mean-quote)**2 for quote in quotes)
    std_dev = (quad_distance/len(quotes))**0.5
    return std_dev >= mean*0.04


def main():
    n = int(input())
    stocks = []
    for _ in range(n):
        line = input().split()
        stocks.append(Stock(name=line[0], quotes=list(map(int, line[1:]))))
    print(*(stock.name for stock in stocks if is_stock_valid(stock.quotes)))

if __name__ == "__main__":
    main()
