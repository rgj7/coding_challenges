"""
CodeAbbey, Problem 11
Coded by whoisrgj
"""


def sum_of_digits(number):
    return sum(map(int, str(number)))


# mathematical method
def sum_of_digits2(number):
    remainder = number
    result = 0
    while remainder > 0:
        result += (remainder % 10)
        remainder //= 10
    return result


def main():
    n = int(input())
    values = [(a*b)+c for a, b, c in [map(int, input().split()) for _ in range(n)]]
    print(*map(sum_of_digits, values))

if __name__ == '__main__':
    main()
