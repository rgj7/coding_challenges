"""
CodeAbbey, Problem 52
Coded by whoisrgj
"""


def triangle_type(a, b, c):
    x, y = a**2 + b**2, c**2
    if x > y:
        return 'A'
    elif x < y:
        return 'O'
    return 'R'


def main():
    n = int(input())
    # results = []
    # for _ in range(n):
    #     a, b, c = map(int, input().split())
    #     results.append(triangle_type(a, b, c))
    # print(" ".join(results))
    print(" ".join([triangle_type(a, b, c)
                    for a, b, c in (map(int, input().split())
                    for _ in range(n))]))

if __name__ == '__main__':
    main()
