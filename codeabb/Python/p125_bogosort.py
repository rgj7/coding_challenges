"""
CodeAbbey, Problem 125
Coded by whoisrgj
"""
from math import factorial


def bogosort(values):
    sorted_values = sorted(values)
    rng = random_number_generator()
    sort_count = 0
    limit = factorial(len(values))
    while sort_count < limit:
        for i in range(len(values)):
            j = next(rng) % len(values)
            values[i], values[j] = values[j], values[i]
        sort_count += 1
        if values == sorted_values:
            return sort_count
    return -1


def random_number_generator(initial_value=918255):
    x = str(initial_value).zfill(6)
    while True:
        y = x[3:] + x[:3]
        x = str(int(x) * int(y)).zfill(12)[3:9]
        yield int(x)


def main():
    n = int(input())
    results = []
    for _ in range(n):
        values = list(map(int, input().split()))
        results.append(bogosort(values))
    print(*results)

if __name__ == '__main__':
    main()
