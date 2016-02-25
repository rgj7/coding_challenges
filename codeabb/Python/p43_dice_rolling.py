"""
CodeAbbey, Problem 28
Coded by Raul Gonzalez
"""


def die_roll(value):
    return int((value * 6)//1 + 1)


def main():
    n = int(input())
    print(*(die_roll(float(input())) for _ in range(n)))

if __name__ == '__main__':
    main()
