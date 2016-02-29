"""
CodeAbbey, Problem 171
Coded by whoisrgj
"""
import math


def tree_height_measurement(distance, degrees):
    return round(distance * math.tan(math.radians(degrees - 90)))


def main():
    n = int(input())
    print(*(tree_height_measurement(a, b) for a, b in (map(float, input().split()) for _ in range(n))))

if __name__ == '__main__':
    main()
