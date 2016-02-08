"""
CodeAbbey, Problem 181
Coded by whoisrgj
"""


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a//b


def mod(a, b):
    return a % b


def sqrt(a):
    return a**0.5


def main():
    tokens = list(input().split())
    tokens.reverse()
    values_stack = list()
    while len(tokens) > 0:
        next_token = tokens.pop()
        try:
            value = int(next_token)
            values_stack.append(value)
        except ValueError:
            b = values_stack.pop()
            if next_token == 'sqrt':
                values_stack.append(sqrt(b))
            else:
                a = values_stack.pop()
                values_stack.append(globals()[next_token](a, b))
    assert len(values_stack) == 1
    print(int(values_stack.pop()))


if __name__ == '__main__':
    main()
