"""
CodeAbbey, Problem 207
Coded by whoisrgj
"""


def main():
    line = input()
    suffixes = [(line[i:], i) for i in range(len(line))]
    print(*(t[1] for t in sorted(suffixes)))

if __name__ == '__main__':
    main()
