"""
CodeAbbey, Problem 34
Coded by Raul Gonzalez
"""
import math


def equation(x, a, b, c, d):
    return a * x + b * math.sqrt(x ** 3) - c * math.exp(-x / 50) - d


def binary_search(a, b, c, d):
    min_value = 0
    x = max_value = 100
    precision = 10**-7

    while min_value + precision < max_value:
        x = (max_value + min_value) / 2
        result = equation(x, a, b, c, d)
        if result < 0:
            min_value = x
        elif result > 0:
            max_value = x
        else:
            break
    return "{:.8f}".format(x)


if __name__ == "__main__":
    N = int(input())
    print(*[binary_search(*map(float, input().split())) for _ in range(N)])

