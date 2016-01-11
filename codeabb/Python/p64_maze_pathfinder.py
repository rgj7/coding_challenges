"""
codeabbey, problem 64
solution by whoisrgj
"""

from collections import deque


class Problem64:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.grid = list()

    def get_input(self):
        self.cols, self.rows = map(int, input().split())
        if not self.rows or not self.cols:
            raise ValueError('rows or cols cannot be 0.')
        for i in range(self.rows):
            self.grid += input()
        if len(self.grid) != self.rows*self.cols:
            raise IOError('incorrect number of values read from input.')

    def in_bounds(self, cell):
        (x, y) = cell
        return 0 <= x < self.rows and 0 <= y < self.cols

    def passable(self, cell):
        (x, y) = cell
        return self.grid[self.index(x, y)] == '1'

    def adjacent_cells(self, cell):
        (x, y) = cell
        adj_cells = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
        adj_cells = filter(self.in_bounds, adj_cells)
        adj_cells = filter(self.passable, adj_cells)
        return adj_cells

    def get_path(self, start, goal):
        frontier = deque()
        frontier.append(start)
        came_from = dict()
        came_from[start] = None

        while len(frontier) != 0:
            current = frontier.popleft()
            if current == goal:
                break
            adj_cells = self.adjacent_cells(current)
            for next_cell in adj_cells:
                if next_cell not in came_from:
                    frontier.append(next_cell)
                    came_from[next_cell] = current

        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    @staticmethod
    def get_direction(x1, y1, x2, y2):
        if x2 == x1+1:
            return 'D'
        if x2 == x1-1:
            return 'U'
        if y2 == y1+1:
            return 'R'
        if y2 == y1-1:
            return 'L'

    def create_directions(self, path):
        directions = []
        (x1, y1) = path[0]
        (x2, y2) = path[1]
        last_direction = self.get_direction(x1, y1, x2, y2)
        count = 1
        for i in range(1, len(path)-1):
            (x1, y1) = path[i]
            (x2, y2) = path[i+1]
            d = self.get_direction(x1, y1, x2, y2)
            if d == last_direction:
                count += 1
            else:
                directions.append("{}{}".format(count, last_direction))
                last_direction = d
                count = 1
        directions.append("{}{}".format(count, last_direction))
        return "".join(directions)

    def print_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.grid[self.index(i, j)], end="")
            print()

    def solve(self):
        self.get_input()

        goal = (0, 0)
        starts = [(0, self.cols-1), (self.rows-1, 0), (self.rows-1, self.cols-1)]
        results = []

        for start in starts:
            path = self.get_path(start, goal)
            results.append(self.create_directions(path))
        print(" ".join(results))

    def index(self, x, y):
        return (self.cols*x)+y


if __name__ == '__main__':
    Problem64().solve()
