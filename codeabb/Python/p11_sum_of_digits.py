"""
CodeAbbey, Problem 11
Coded by whoisrgj
"""


def sum_of_digits(number):
    """string to int"""
    return sum(map(int, str(number)))


def sum_of_digits_math(number):
    """mathematical"""
    remainder = number
    result = 0
    while remainder > 0:
        result += (remainder % 10)
        remainder //= 10
    return result


def main():
    n = int(input())
    results = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        results.append(sum_of_digits(a * b + c))
    print(*results)

if __name__ == '__main__':
    main()
