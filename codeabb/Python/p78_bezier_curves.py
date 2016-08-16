"""
CodeAbbey, Problem 78
Coded by whoisrgj
"""
from collections import namedtuple

Point = namedtuple('Point', 'x y')


def calculate_point(p0, p1, alpha):
    x = alpha * (p1.x - p0.x)
    y = alpha * (p1.y - p0.y)
    return Point(p0.x + x, p0.y + y)


def get_bc_point(points, alpha):
    if len(points) <= 2:
        return calculate_point(points[0], points[1], alpha)
    new_points = [calculate_point(points[i - 1], points[i], alpha)
                  for i in range(1, len(points))]
    return get_bc_point(new_points, alpha)


def main():
    m, n = map(int, input().split())
    points = [Point(*map(int, input().split())) for _ in range(m)]
    step = 1.0 / (n - 1)
    bc_points = (get_bc_point(points, step*i) for i in range(n))
    print(*("{} {}".format(round(p.x), round(p.y)) for p in bc_points))

if __name__ == '__main__':
    main()
