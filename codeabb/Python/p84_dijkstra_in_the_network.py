"""
CodeAbbey, Problem 84
Coded by whoisrgj
"""
from collections import defaultdict


def linear_congruential_generator(a=445, c=700001, m=2097152, x=0):
    while True:
        x = (a * x + c) % m
        yield x


def generate_graph(vertices, initial_seed):
    graph = defaultdict(dict)
    lcg = linear_congruential_generator(x=initial_seed)
    for vi in range(1, vertices + 1):
        v1, d1, v2, d2 = map(
            lambda x: (x % vertices) + 1,
            (next(lcg) for _ in range(4)))
        args = [(vi, v1, d1), (vi, v2, d2), (v1, vi, d1), (v2, vi, d2)]
        for i, v, d in args:
            if i == v or (i in graph and v in graph[i]):
                continue
            graph[i][v] = d
    return graph


def find_all_shortest(start, graph):
    vertices, dist = set(), dict()
    for v in graph:
        dist[v] = float("inf")
        vertices.add(v)
    dist[start] = 0
    while vertices:
        u = min(vertices, key=dist.get)
        vertices.remove(u)
        for v, l in graph[u].items():
            alt = dist[u] + l
            if alt < dist[v]:
                dist[v] = alt
    return dist


def main():
    vertices, initial_seed, start = map(int, input().split())
    graph = generate_graph(vertices, initial_seed)
    print(*find_all_shortest(start, graph).values())


if __name__ == '__main__':
    main()
