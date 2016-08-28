"""
CodeAbbey, Problem 154
Coded by whoisrgj
"""
from collections import defaultdict, deque


def breadth_first_search(graph):
    queue = deque([0])
    seen = {0: -1}
    while queue:
        current = queue.popleft()
        for neighbor in sorted(graph[current]):
            if neighbor not in seen:
                queue.append(neighbor)
                seen[neighbor] = current
    return seen.values()


def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(*breadth_first_search(graph))


if __name__ == '__main__':
    main()
