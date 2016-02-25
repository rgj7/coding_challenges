"""
CodeAbbey, Problem 50
Coded by Raul Gonzalez
"""


def is_palindrome(s: str):
    stripped_string = "".join(c for c in s.lower() if str.isalnum(c))
    return 'Y' if stripped_string == stripped_string[::-1] else 'N'


def main():
    n = int(input())
    print(" ".join(is_palindrome(input()) for _ in range(n)))

if __name__ == '__main__':
    main()
