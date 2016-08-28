"""
CodeAbbey, Problem 51
Coded by whoisrgj
"""


def main():
    results = []
    for _ in range(3):
        die_values = list(map(int, input().split()))
        die_values.pop()  # remove 0 at end
        dies = min(die_values)
        sides = max(die_values) // dies
        results.append("{0}d{1}".format(dies, sides))
    print(*results)


if __name__ == '__main__':
    main()
