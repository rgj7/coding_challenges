"""
CodeAbbey, Problem 47
Coded by whoisrgj
"""

import string


def caesar_shift_cipher(s, k):
    shifted_letters = string.ascii_uppercase[k:] + string.ascii_uppercase[:k]
    table = str.maketrans(shifted_letters, string.ascii_uppercase)
    return s.translate(table)


def main():
    n, k = map(int, input().split())
    print(" ".join([caesar_shift_cipher(input(), k) for _ in range(n)]))

if __name__ == '__main__':
    main()
