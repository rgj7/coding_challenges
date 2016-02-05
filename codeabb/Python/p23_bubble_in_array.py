"""
CodeAbbey, Problem 23
Coded by whoisrgj
"""


def calculate_checksum(values, seed, limit):
    result = 0
    for value in values:
        result += value
        result *= seed
        result %= limit
    return result


def solve(values):
    swaps = 0
    for i in range(1, len(values)):
        if values[i-1] > values[i]:
            values[i-1], values[i] = values[i], values[i-1]  # swap
            swaps += 1
    return swaps, calculate_checksum(values, 113, 10000007)


if __name__ == '__main__':
    array_values = list(map(int, input().split()))
    array_values.pop()  # remove -1 at end of list
    print(*solve(array_values))
