"""
CodeAbbey, Problem 19
Coded by whoisrgj
"""

bracket_pairs = {'[': ']', '{': '}', '<': '>', '(': ')'}


def has_valid_brackets(string):
    stack = []
    for c in string:
        if c in bracket_pairs:  # add bracket start to stack
            stack.append(c)
        elif c in bracket_pairs.values():  # if bracket end
            if not len(stack):  # there should be at least 1 bracket start
                return 0
            key = stack.pop()
            if bracket_pairs[key] != c:  # pair doesn't match
                return 0
    if len(stack):  # any remaining brackets is invalid
        return 0
    return 1


def main():
    n = int(input())
    print(*(has_valid_brackets(input()) for _ in range(n)))

if __name__ == '__main__':
    main()
