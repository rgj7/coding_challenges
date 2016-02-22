"""
CodeAbbey, Problem 131
Coded by whoisrgj
"""
from collections import Counter


def get_valid_word_count(length, letters):
    count = 0
    with open('words.txt') as f:
        for line in f:
            word = line.rstrip()
            if len(word) == length:
                counter = Counter(word)  # counter for characters in word
                counter.subtract(letters)  # for each char in letters, reduce in counter
                if not len(+counter):  # +counter: removes values 0 or less. len should be 0.
                    count += 1
    return count


def main():
    n = int(input())
    results = []
    for _ in range(n):
        letters = input().split()
        length = int(letters.pop(0))
        results.append(get_valid_word_count(length, letters))
    print(*results)

if __name__ == '__main__':
    main()
