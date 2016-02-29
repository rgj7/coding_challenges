"""
CodeAbbey, Problem 104
Coded by whoisrgj
"""
from collections import namedtuple
import math

# using namedtuple for practice
Point = namedtuple('Point', 'x y')


def triangle_area(p1: Point, p2: Point, p3: Point):
    a = math.sqrt(math.pow(p2.x - p1.x, 2) + math.pow(p2.y - p1.y, 2))
    b = math.sqrt(math.pow(p3.x - p2.x, 2) + math.pow(p3.y - p2.y, 2))
    c = math.sqrt(math.pow(p1.x - p3.x, 2) + math.pow(p1.y - p3.y, 2))
    s = (a + b + c) / 2
    return "{:.8g}".format(math.sqrt(s * (s - a) * (s - b) * (s - c)))


# formula from author's notes, abs value of the vector product divided by 2
def triangle_area2(p1: Point, p2: Point, p3: Point):
    p = p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
    return "{:.8g}".format(abs(p) / 2)


def main():
    n = int(input())
    results = []
    for _ in range(n):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        p1, p2, p3 = Point(x1, y1), Point(x2, y2), Point(x3, y3)
        results.append(triangle_area2(p1, p2, p3))
    print(" ".join(results))

if __name__ == '__main__':
    main()
