"""
CodeAbbey, Problem 171
Coded by whoisrgj
"""
import math


def tree_height_measurement(distance, degrees):
    return round(distance * math.tan(math.radians(degrees - 90)))


def main():
    n = int(input())
    results = []
    for _ in range(n):
        dist, deg = map(float, input().split())
        results.append(tree_height_measurement(dist, deg))
    print(*results)

if __name__ == '__main__':
    main()
