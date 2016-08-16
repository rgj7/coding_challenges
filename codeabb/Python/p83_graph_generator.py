"""
CodeAbbey, Problem 83
Coded by whoisrgj
"""
from collections import defaultdict


class GraphGenerator(object):

    def __init__(self, vertices, initial_seed):
        self.graph = defaultdict(dict)
        self.vertices = vertices
        self.lcg = self.linear_congruential_generator(x=initial_seed)

    @staticmethod
    def linear_congruential_generator(a=445, c=700001, m=2097152, x=0):
        while True:
            x = (a * x + c) % m
            yield x

    def generate_graph(self):
        for vi in range(1, self.vertices + 1):
            v1, d1, v2, d2 = map(
                lambda x: (x % self.vertices) + 1,
                (next(self.lcg) for _ in range(4)))
            args = [(vi, v1, d1), (vi, v2, d2), (v1, vi, d1), (v2, vi, d2)]
            for i, v, d in args:
                if i == v:
                    continue
                if i in self.graph and v in self.graph[i]:
                    continue
                self.graph[i][v] = d

    def sum_of_weights(self):
        return [sum(x.values()) for x in self.graph.values()]


def main():
    vertices, initial_seed = map(int, input().split())
    gg = GraphGenerator(vertices, initial_seed)
    gg.generate_graph()
    print(*gg.sum_of_weights())


if __name__ == '__main__':
    main()
