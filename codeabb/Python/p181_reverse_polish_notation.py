"""
CodeAbbey, Problem 181
Coded by whoisrgj
"""

from collections import deque


def main():
    tokens = deque(input().split())
    values = list()
    operations = {
        "add": "a+b",
        "sub": "a-b",
        "mul": "a*b",
        "div": "a//b",
        "mod": "a%b",
        "sqrt": "b**0.5"
    }
    while tokens:
        token = tokens.popleft()
        try:
            values.append(int(token))
        except ValueError:  # operation
            b = values.pop()
            a = None if token == "sqrt" else values.pop()
            values.append(int(eval(operations[token])))
    assert len(values) == 1
    print(values.pop())

if __name__ == '__main__':
    main()
