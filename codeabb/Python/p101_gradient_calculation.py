"""
CodeAbbey, Problem 101
Coded by whoisrgj
"""
from math import exp, atan2, degrees


class Gradient(object):
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c

    def f(self, x, y):
        e = -(x + self.A)**2 - (y + self.B)**2
        return (x - self.A)**2 + (y - self.B)**2 + self.C * exp(e)

    def descent(self, x, y, dt=1e-9):
        f0 = self.f(x, y)
        f1 = self.f(x + dt, y)
        f2 = self.f(x, y + dt)
        x1, y1 = (f1 - f0) / dt, (f2 - f0) / dt
        return round(180 + degrees(atan2(y1, x1)))


def main():
    n, a, b, c = map(float, input().split())
    g = Gradient(a, b, c)
    results = []
    for _ in range(int(n)):
        x, y = map(float, input().split())
        results.append(g.descent(x, y))
    print(*results)

if __name__ == '__main__':
    main()
