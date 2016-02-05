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
            if len(stack) < 1:  # there should be at least 1 bracket start
                return 0
            key = stack.pop()
            if bracket_pairs[key] != c:  # pair doesn't match
                return 0
    if len(stack) > 0:  # any remaining brackets is invalid
        return 0
    return 1


if __name__ == '__main__':
    N = int(input())
    results = list()
    for _ in range(N):
        results.append(str(has_valid_brackets(input())))
    print(" ".join(results))
