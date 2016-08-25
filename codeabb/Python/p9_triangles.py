"""
CodeAbbey, Problem 9
Coded by whoisrgj
"""


def is_triangle(a, b, c):
    return a+b >= c and a+c >= b and b+c >= a


def main():
    n = int(input())
    results = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        results.append(int(is_triangle(a, b, c)))
    print(*results)

if __name__ == '__main__':
    main()
