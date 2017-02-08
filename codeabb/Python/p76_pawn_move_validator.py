"""
CodeAbbey, Problem 76
Coded by whoisrgj
"""

from collections import namedtuple

Move = namedtuple('Move', 'source destination')
Coordinate = namedtuple('Coordinate', 'col row')


class PawnMoveValidator(object):
    def __init__(self):
        self.pieces = dict()
        self.setup()

    def setup(self):
        rank_order = 'rnbqkbnr'
        for x in range(1, 9):
            self.pieces[Coordinate(x, 8)] = rank_order[x-1]
            self.pieces[Coordinate(x, 7)] = 'p'
            self.pieces[Coordinate(x, 2)] = 'P'
            self.pieces[Coordinate(x, 1)] = rank_order[x-1].upper()

    def process_moves(self, moves: list):
        for step, move in enumerate(moves, start=1):
            if self.is_valid_move(move):
                self.move(move)
            else:
                return step
        return 0

    def move(self, move: Move):
        self.pieces[move.destination] = self.pieces[move.source]
        del self.pieces[move.source]

    def is_valid_move(self, move: Move):
        # we're only validating pawns, all else is considered correct
        if self.is_pawn(move.source):
            return self.validate_pawn_move(move)
        return True

    def validate_pawn_move(self, move: Move):
        delta, start_row = (-1, 7) if self.is_black(move.source) else (1, 2)
        left = Coordinate(move.source.col-1, move.source.row+delta)
        right = Coordinate(move.source.col+1, move.source.row+delta)
        up_one = Coordinate(move.source.col, move.source.row+delta)
        up_two = Coordinate(move.source.col, move.source.row+(delta*2))
        if move.destination == up_one:
            if self.is_occupied(move.destination):
                return False
        elif move.destination == up_two:
            if not move.source.row == start_row:
                return False
            for row in range(move.source.row, move.destination.row, delta):
                if self.is_occupied(Coordinate(move.source.col, row+delta)):
                    return False
        elif move.destination in (left, right):
            if self.is_occupied(move.destination) and not self.is_enemy(move):
                return False
        else:  # not a valid pawn move
            return False
        return True

    def is_occupied(self, coord: Coordinate):
        return coord in self.pieces

    def is_enemy(self, move: Move):
        if self.is_black(move.source) and self.is_white(move.destination):
            return True
        if self.is_white(move.source) and self.is_black(move.destination):
            return True
        return False

    def is_pawn(self, coord: Coordinate):
        return self.pieces[coord].lower() == 'p'

    def is_black(self, coord: Coordinate):
        return self.pieces[coord].islower()

    def is_white(self, coord: Coordinate):
        return self.pieces[coord].isupper()

    @staticmethod
    def parse_moves(moves: list):
        columns = {v: k for k, v in enumerate("abcdefgh", start=1)}
        parsed_moves = []
        for move in moves:
            source = Coordinate(columns[move[0]], int(move[1]))
            destination = Coordinate(columns[move[2]], int(move[3]))
            parsed_moves.append(Move(source, destination))
        return parsed_moves


def main():
    test_cases = int(input())
    results = []
    for _ in range(test_cases):
        parsed_moves = PawnMoveValidator.parse_moves(moves=input().split())
        results.append(PawnMoveValidator().process_moves(moves=parsed_moves))
    print(*results)

if __name__ == '__main__':
    main()
