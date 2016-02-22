"""
CodeAbbey, Problem 20
Coded by whoisrgj
"""


def count_vowels(string):
    return sum(1 for c in string if c in 'aeiouy')


def main():
    n = int(input())
    print(*(count_vowels(input()) for _ in range(n)))

if __name__ == '__main__':
    main()
