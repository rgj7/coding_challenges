"""
CodeAbbey, Problem 85
Coded by whoisrgj
"""
import math


class Star(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Problem85(object):
    def __init__(self, stars):
        self.stars = stars

    def rotate(self, angle):
        radians = math.radians(angle)
        for star in self.stars:
            x = round(
                (star.x * math.cos(radians)) - (star.y * math.sin(radians)))
            y = round(
                (star.x * math.sin(radians)) + (star.y * math.cos(radians)))
            star.x, star.y = x, y

    def __str__(self):
        sorted_stars = sorted(self.stars, key=lambda s: (s.y, s.x))
        return " ".join(star.name for star in sorted_stars)


def main():
    n, angle = map(int, input().split())
    stars = []
    for _ in range(n):
        name, x, y = input().split()
        stars.append(Star(name, int(x), int(y)))
    p = Problem85(stars)
    p.rotate(angle)
    print(p)

if __name__ == '__main__':
    main()
