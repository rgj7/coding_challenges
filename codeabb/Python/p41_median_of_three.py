"""
CodeAbbey, Problem 41
Coded by whoisrgj
"""


def main():
    n = int(input())
    print(*(sorted(map(int, input().split()))[1] for _ in range(n)))

if __name__ == '__main__':
    main()
