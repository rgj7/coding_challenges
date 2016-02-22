"""
CodeAbbey, Problem 94
Coded by whoisrgj
"""


def main():
    n = int(input())
    print(*[sum([x**2 for x in list(map(int, input().split()))]) for _ in range(n)])

if __name__ == '__main__':
    main()
