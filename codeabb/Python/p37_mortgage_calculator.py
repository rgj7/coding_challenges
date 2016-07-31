"""
CodeAbbey, Problem 37
Coded by whoisrgj
"""

import math


def calculate_monthly_payment(principle, interest_rate, months):
    monthly_interest = interest_rate/1200
    x = (1+monthly_interest)**months
    monthly_payment = principle*((monthly_interest*x)/(x-1))
    return math.ceil(monthly_payment)


def main():
    print(calculate_monthly_payment(*map(int, input().split())))

if __name__ == "__main__":
    main()
