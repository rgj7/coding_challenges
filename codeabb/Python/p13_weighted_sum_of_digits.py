"""
CodeAbbey, Problem 13
Coded by whoisrgj
"""


def wsd(num_str):
    return sum(i*int(d) for i, d in enumerate(num_str, 1))


def main():
    input()  # N, not used
    print(*(wsd(num_str) for num_str in input().split()))


if __name__ == '__main__':
    main()
