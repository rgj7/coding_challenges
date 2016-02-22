"""
CodeAbbey, Problem 24
Coded by whoisrgj
"""


def nrg(value):
    results = set()
    result = value
    while result not in results:
        yield result
        results.add(result)
        result = str(int(result)**2).zfill(8)[2:6]


def main():
    n = int(input())  # not used
    values = list(input().split())
    print(*(sum(1 for i in nrg(value)) for value in values))

if __name__ == '__main__':
    main()
