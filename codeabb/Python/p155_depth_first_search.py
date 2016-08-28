"""
CodeAbbey, Problem 155
Coded by whoisrgj
"""
from collections import defaultdict


def depth_first_search(graph):
    stack = [(0, -1)]
    seen = {}
    while stack:
        current, from_ = stack.pop()
        if current not in seen:
            seen[current] = from_
            for neighbor in sorted(graph[current], reverse=True):
                stack.append((neighbor, current))
    return seen.values()


def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(*depth_first_search(graph))


if __name__ == '__main__':
    main()
