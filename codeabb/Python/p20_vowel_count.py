"""
CodeAbbey, Problem 20
Coded by whoisrgj
"""

VOWEL_SET = set('aeiouy')


def count_vowels(string):
    return sum([string.count(vowel) for vowel in VOWEL_SET])

if __name__ == '__main__':
    N = int(input())
    results = [str(count_vowels(input())) for _ in range(N)]
    print(" ".join(results))
