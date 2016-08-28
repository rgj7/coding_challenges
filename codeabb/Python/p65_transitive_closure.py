"""
CodeAbbey, Problem 65
Coded by whoisrgj
"""


def main():
    n = int(input())
    candy_states = set()
    roads = list()
    for _ in range(n):
        road = tuple(map(str.strip, input().split('-')))
        candy_states.update(road)
        roads.append(road)
    # build matrix
    m = []
    for i in range(len(candy_states)):
        row = []
        for j in range(len(candy_states)):
            row.append(0 if i == j else int(10e7))
        m.append(row)
    # add roads
    cs = {k: v for v, k in enumerate(candy_states)}
    for a, b in roads:
        m[cs[a]][cs[b]] = 1
        m[cs[b]][cs[a]] = 1
    # calculate shortest path
    for k in range(len(candy_states)):
        for i in range(len(candy_states)):
            for j in range(len(candy_states)):
                if m[i][j] > m[i][k] + m[k][j]:
                    m[i][j] = m[i][k] + m[k][j]
    # gather test cases
    n = int(input())
    results = []
    for _ in range(n):
        a, b = map(str.strip, input().split('-'))
        results.append(m[cs[a]][cs[b]])
    print(*results)

if __name__ == '__main__':
    main()
