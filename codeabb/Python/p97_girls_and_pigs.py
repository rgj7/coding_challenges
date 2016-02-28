"""
CodeAbbey, Problem 97
Coded by whoisrgj
"""


def girls_and_pigs(legs, breasts):
    solutions = 0
    max_pigs = legs // 4
    for pigs in range(1, max_pigs + 1):  # we assume solutions must contain one of each
        girls = (legs - (pigs * 4)) // 2
        if girls:  # we assume solutions must contain one of each
            remaining_breasts = breasts - (girls * 2)
            if remaining_breasts % pigs == 0 and (remaining_breasts // pigs) % 2 == 0:  # pigs must have even breasts
                solutions += 1
    return solutions


def main():
    n = int(input())
    print(*(girls_and_pigs(legs, breasts)
            for legs, breasts in (map(int, input().split())
                                  for _ in range(n))))

if __name__ == '__main__':
    main()
