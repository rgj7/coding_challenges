"""
CodeAbbey, Problem 93
Coded by whoisrgj
"""
from heapq import heappop, heappush


class StarvingPQ(object):
    def __init__(self, visitor_count, initial_seed):
        self.lcg = self.linear_congruential_generator(x=initial_seed)
        self.personal_discomfort_sum = 0
        self.pq = []
        self.visitor_count = visitor_count

    def start(self):
        for t in range((2*self.visitor_count)+1):
            if self.pq and t % 2 == 0:
                self.feed_visitor(t)
            if t < self.visitor_count:
                self.add_visitor(t)

    def add_visitor(self, arrival_time):
        starvation_degree = (next(self.lcg) % 999) + 1
        # negating starvation degree to utilize min-heap as max-heap
        heappush(self.pq, (-starvation_degree, arrival_time))

    def feed_visitor(self, feeding_time):
        starvation_degree, arrival_time = heappop(self.pq)
        personal_discomfort = -starvation_degree * (feeding_time-arrival_time)
        self.personal_discomfort_sum += personal_discomfort

    @staticmethod
    def linear_congruential_generator(a=445, c=700001, m=2097152, x=0):
        while True:
            x = (a * x + c) % m
            yield x


def main():
    n, x0 = map(int, input().split())
    spq = StarvingPQ(visitor_count=n, initial_seed=x0)
    spq.start()
    print(spq.personal_discomfort_sum)


if __name__ == '__main__':
    main()
