"""
CodeAbbey, Problem 17
Coded by whoisrgj
"""


def calculate_checksum(values):
    result = 0
    for value in values:
        result += value
        result *= 113
        result %= 10000007
    return result


def main():
    n = int(input())
    array_values = list(map(int, input().split()))
    print(calculate_checksum(array_values))

if __name__ == '__main__':
    main()
