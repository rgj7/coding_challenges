"""
CodeAbbey, Problem 211
Coded by whoisrgj
"""
from collections import Counter
from math import log2


def calculate_entropy(string):
    counter = Counter(string)
    frequency = {key: (value/len(string)) for key, value in counter.items()}
    return sum(frequency[k] * -log2(frequency[k]) for k in frequency)


def main():
    n = int(input())
    results = []
    for _ in range(n):
        results.append(calculate_entropy(input()))
    print(*results)

if __name__ == '__main__':
    main()
