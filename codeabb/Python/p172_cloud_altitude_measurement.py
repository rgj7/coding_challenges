"""
CodeAbbey, Problem 172
Coded by whoisrgj
"""
import math


def cloud_altitude(d1, a, b):
    tan_a = math.tan(math.radians(a))
    tan_b = math.tan(math.radians(b))
    d2 = (tan_a * d1) / (tan_b - tan_a)
    return round(tan_b * d2)


def main():
    n = int(input())
    print(*(cloud_altitude(*map(float, input().split())) for _ in range(n)))

if __name__ == '__main__':
    main()
