"""
CodeAbbey, Problem 47
Coded by whoisrgj
"""
from string import ascii_uppercase


def caesar_shift_cipher(s, k):
    shifted_letters = ascii_uppercase[k:] + ascii_uppercase[:k]
    table = s.maketrans(shifted_letters, ascii_uppercase)
    return s.translate(table)


def main():
    n, k = map(int, input().split())
    print(" ".join(caesar_shift_cipher(input(), k) for _ in range(n)))

if __name__ == '__main__':
    main()
