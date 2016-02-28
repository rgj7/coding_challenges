"""
CodeAbbey, Problem 105
Coded by whoisrgj
"""
from collections import namedtuple

Point = namedtuple('Point', 'x y')


def triangle_area(p1: Point, p2: Point, p3: Point):
    p = p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
    return abs(p) / 2


def convex_polygon_area(points):
    return sum(triangle_area(points[0], points[i+1], points[i+2]) for i in range(len(points)-2))


def main():
    n = int(input())
    points = [Point(x, y) for x, y in (map(int, input().split()) for _ in range(n))]
    print(convex_polygon_area(points))

if __name__ == '__main__':
    main()
