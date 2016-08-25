"""
CodeAbbey, Problem 54
Coded by whoisrgj
"""
from math import sqrt, floor


def main():
    tc = int(input())
    results = []
    for _ in range(tc):
        number = int(input())
        sqrt_ = floor(sqrt(number))
        for n in range(1, sqrt_ + 1):
            for m in range(n + 1, sqrt_ + 1):
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                if a+b+c == number:
                    results.append(c ** 2)
    print(*results)

if __name__ == '__main__':
    main()
