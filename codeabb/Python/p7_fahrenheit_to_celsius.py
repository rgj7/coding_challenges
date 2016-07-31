"""
CodeAbbey, Problem 7
Coded by whoisrgj
"""


def to_celsius(f): return round((f - 32) / 1.8)


def main():
    f_values = list(map(int, input().split()))
    f_values.pop(0)  # ignore initial N value
    print(*(to_celsius(f) for f in f_values))

if __name__ == '__main__':
    main()
