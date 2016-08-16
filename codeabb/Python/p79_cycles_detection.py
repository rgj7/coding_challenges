"""
CodeAbbey, Problem 79
Coded by whoisrgj
"""
from collections import defaultdict


class CycleDetection(object):
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    def transverse(self):
        cities = self.graph.keys()
        for city in cities:
            self.visited.add(city)
            next_cities = [
                c for c in self.graph[city] if c not in self.visited]





def main():
    n = int(input())
    tokens = input().split()
    graph = defaultdict(list)
    for road_desc in tokens[1:]:
        a, b = road_desc.split("-")
        graph[a].append(b)
        graph[b].append(a)
    print(graph)


if __name__ == '__main__':
    main()
