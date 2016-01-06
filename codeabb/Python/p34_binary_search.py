"""
CodeAbbey, Problem 34
Coded by Raul Gonzalez
"""
import math


class Problem34:
    def __init__(self):
        pass

    @staticmethod
    def binary_search(x, a, b, c, d):
        return a * x + b * math.sqrt(x ** 3) - c * math.exp(-x / 50) - d

    def solve(self):
        test_cases = int(input())
        for i in range(test_cases):
            a, b, c, d = map(float, input().split())
            min_value = 0
            x = max_value = 100
            precision = 10**-7

            while min_value + precision < max_value:
                x = (max_value + min_value) / 2
                result = self.binary_search(x, a, b, c, d)
                if result < 0:
                    min_value = x
                elif result > 0:
                    max_value = x
                else:
                    break
            print("{:.8f}".format(x), end=" ")


if __name__ == "__main__":
    Problem34().solve()
