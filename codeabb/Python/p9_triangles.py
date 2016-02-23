"""
CodeAbbey, Problem 9
Coded by whoisrgj
"""


def is_triangle(a, b, c):
    return a+b >= c and a+c >= b and b+c >= a


def main():
    n = int(input())
    # results = []
    # for _ in range(n):
    #     a, b, c = map(int, input().split())
    #     results.append(is_triangle(a, b, c))
    # print(*map(int, results))
    print(*map(int, (is_triangle(*map(int, input().split())) for _ in range(n))))

if __name__ == '__main__':
    main()
