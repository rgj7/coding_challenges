"""
CodeAbbey, Problem 85
Coded by whoisrgj
"""
from collections import namedtuple
import math

Star = namedtuple('Star', 'name x y')


class Problem85(object):
    def __init__(self, stars):
        self.stars = stars

    def rotate(self, angle):
        rotated_stars = []
        radians = math.radians(angle)
        for star in self.stars:
            x = round((star.x * math.cos(radians)) - (star.y * math.sin(radians)))
            y = round((star.x * math.sin(radians)) + (star.y * math.cos(radians)))
            rotated_stars.append(Star(star.name, x, y))
        self.stars = rotated_stars

    def __str__(self):
        return " ".join(star.name for star in sorted(self.stars, key=lambda s: (s.y, s.x)))


def main():
    n, angle = map(int, input().split())
    stars = [Star(name, int(x), int(y)) for name, x, y in (input().split() for _ in range(n))]
    p = Problem85(stars)
    p.rotate(angle)
    print(p)

if __name__ == '__main__':
    main()
