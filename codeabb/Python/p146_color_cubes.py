"""
CodeAbbey, Problem 146
Coded by whoisrgj
"""


class ColorCubes(object):

    T = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, game_field, size):
        self.game_field = game_field
        self.size = size
        self.score = 0
        self.count = 1
        self.affected_cols = set()

    def perform_move(self, col, row):
        value = self.get_cube_value(col, row)
        self.eliminate_cubes(col, row, value)
        self.update_score()
        empty_cols = []
        for col in self.affected_cols:
            if self.shift_down(col):  # returns True if column is empty
                empty_cols.append(col)
        for i, col in enumerate(sorted(empty_cols)):
            self.shift_left(col-i)
        self.affected_cols.clear()

    def eliminate_cubes(self, col, row, value):
        self.update_cube_value(col, row, '-')
        self.affected_cols.add(col)
        for tc, tr in self.T:
            c, r = col + tc, row + tr
            if (0 <= c < self.size) and (0 <= r < self.size):
                if self.get_cube_value(c, r) == value:
                    self.count += 1
                    self.eliminate_cubes(c, r, value)

    def shift_down(self, col):
        col_values = []
        for row in range(self.size - 1, -1, -1):
            value = self.get_cube_value(col, row)
            if value != '-':
                col_values.append(value)
        if col_values:
            for row in range(self.size):
                try:
                    value = col_values.pop()
                except IndexError:
                    value = '-'
                self.update_cube_value(col, row, value)
            return False
        return True

    def shift_left(self, col):
        for row in range(self.size):
            del self.game_field[row][col]
            self.game_field[row].append('-')

    def update_score(self):
        self.score += self.count * (self.count + 1) // 2
        self.count = 1

    def update_cube_value(self, col, row, value):
        self.game_field[self.size - row - 1][col] = value

    def get_cube_value(self, col, row):
        return self.game_field[self.size - row - 1][col]

    def print_field(self):
        for row in self.game_field:
            print(" ".join(row))


def main():
    # gather inputs
    size = int(input())
    game_field = []
    for _ in range(size):
        game_field.append([c for c in input()])
    move_count = int(input())
    moves = []
    for move in input().split(','):
        col, row = map(int, move.split())
        moves.append((col, row))
    assert move_count == len(moves)
    # start game
    cc = ColorCubes(game_field, size)
    for move in moves:
        # print("MOVE:", move)
        # print("BEFORE: ")
        # cc.print_field()
        cc.perform_move(*move)
        # print("AFTER: ")
        # cc.print_field()
        # print()
    print(cc.score)

if __name__ == '__main__':
    main()
