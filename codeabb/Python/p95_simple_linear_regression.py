"""
CodeAbbey, Problem 95
Coded by whoisrgj
"""
from collections import namedtuple

Record = namedtuple('Record', 'days, price')


def main():
    a, b = map(int, input().split())
    data = []
    for _ in range(b-a+1):
        year, values = input().split(":")
        days, price = map(int, values.split())
        data.append(Record(days, price))
    # calculate
    days_mean = sum(record.days for record in data)/len(data)
    prices_mean = sum(record.price for record in data)/len(data)
    numerator = sum((record.days - days_mean)*(record.price - prices_mean)
                    for record in data)
    denominator = sum((record.days-days_mean)**2 for record in data)
    k = numerator/denominator
    b = prices_mean - (k*days_mean)
    print(k, b)

if __name__ == '__main__':
    main()
