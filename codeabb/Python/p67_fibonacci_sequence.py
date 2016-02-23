"""
CodeAbbey, Problem 67
Coded by whoisrgj
"""

import math


def get_fibonacci_index(fibonacci_value):
    idx = round(math.log(fibonacci_value * math.sqrt(5) + 0.5, (1 + math.sqrt(5)) / 2))
    return idx if idx > 0 else 0


def main():
    n = int(input())
    print(*(get_fibonacci_index(int(input())) for _ in range(n)))

if __name__ == '__main__':
    main()
