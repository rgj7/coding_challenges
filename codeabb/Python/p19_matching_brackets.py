"""
CodeAbbey, Problem 19
Coded by whoisrgj
"""


def has_valid_brackets(string):
    bracket_pairs = {'[': ']', '{': '}', '<': '>', '(': ')'}
    stack = []
    for c in string:
        if c in bracket_pairs:  # add bracket start to stack
            stack.append(c)
        elif c in bracket_pairs.values():  # if bracket end
            if not stack:  # there should be at least 1 bracket start
                return 0
            key = stack.pop()
            if bracket_pairs[key] != c:  # pair doesn't match
                return 0
    if stack:  # any remaining brackets is invalid
        return 0
    return 1


def main():
    n = int(input())
    print(*(has_valid_brackets(input()) for _ in range(n)))

if __name__ == '__main__':
    main()
