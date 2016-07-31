"""
CodeAbbey, Problem 35
Coded by whoisrgj
"""


def truncate_float(value, precision):
    """ugly way to truncate (not round) a float at certain precision"""
    a, b = str(value).split('.')
    return float("{}.{}".format(a, b[:precision]))


def calculate_years(starting_sum, required_sum, interest_rate):
    current_sum = starting_sum
    years = 0
    while required_sum > current_sum:
        current_sum += current_sum*(interest_rate/100)
        current_sum = truncate_float(current_sum, 2)
        years += 1
    return years


def main():
    n = int(input())
    results = []
    for _ in range(n):
        s, r, p = map(int, input().split())
        results.append(calculate_years(s, r, p))
    print(*results)


if __name__ == '__main__':
    main()
