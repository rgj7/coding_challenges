"""
codeabbey, problem 76
solution by whoisrgj
"""

from enum import Enum
import re


class Type(Enum):
    KING = 'K'
    QUEEN = 'Q'
    KNIGHT = 'N'
    BISHOP = 'B'
    ROOK = 'R'
    PAWN = 'P'


class Side(Enum):
    WHITE = 'W'
    BLACK = 'B'


class ChessPiece:
    def __init__(self, piece_type: Type, side: Side):
        self.piece_type = piece_type
        self.side = side


class ChessBoard:
    def __init__(self):
        self.board = [None]*64
        self.set_up_pieces()

    def set_up_pieces(self):
        types = [Type.ROOK, Type.KNIGHT, Type.BISHOP, Type.QUEEN, Type.KING, Type.BISHOP, Type.KNIGHT, Type.ROOK]
        for i in range(8):
            self.board[i] = ChessPiece(types[i], Side.BLACK)
            self.board[8+i] = ChessPiece(Type.PAWN, Side.BLACK)
            self.board[48+i] = ChessPiece(Type.PAWN, Side.WHITE)
            self.board[56+i] = ChessPiece(types[i], Side.WHITE)

    def set_piece(self, x, y, piece):
        self.board[(8*x)+y] = piece

    def get_piece(self, x, y) -> ChessPiece:
        return self.board[(8*x)+y]

    def is_enemy(self, x, y, current_side):
        return not self.get_piece(x, y).side == current_side

    def is_occupied(self, x, y):
        return self.get_piece(x, y) is not None

    @staticmethod
    def in_bounds(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def valid_turn(self, move_from, turn):
        (x1, y1) = move_from
        from_piece = self.get_piece(x1, y1)
        if from_piece.side == Side.WHITE:
            return turn % 2 == 1
        else:
            return turn % 2 == 0

    def valid_move(self, move_from, move_to):
        (x1, y1) = move_from
        (x2, y2) = move_to
        # check bounds
        if not self.in_bounds(x1, y1) or not self.in_bounds(x2, y2):
            return False
        from_piece = self.get_piece(x1, y1)
        # we're only interested in pawns
        if from_piece.piece_type == Type.PAWN:
            if from_piece.side == Side.WHITE:
                d_offset, start_row = -1, 6  # move up
            else:
                d_offset, start_row = 1, 1  # move down
            # check each of four possible moves
            if x1+(1*d_offset) == x2 and y1 == y2 and not self.is_occupied(x2, y2):
                return True
            if x1 == start_row and x1+(2*d_offset) == x2 and y1 == y2 \
                    and (not self.is_occupied(x2, y2) and not self.is_occupied(x1+(1*d_offset), y2)):
                return True
            if x1+(1*d_offset) == x2 and (y1-1 == y2 or y1+1 == y2) and self.is_enemy(x2, y2, from_piece.side):
                return True
        else:
            return True  # all other moves by non-pawns are considered correct
        return False

    def move_piece(self, move_from, move_to):
        (x1, y1) = move_from
        (x2, y2) = move_to
        from_piece = self.get_piece(x1, y1)
        self.set_piece(x2, y2, from_piece)
        self.set_piece(x1, y1, None)


class Problem76:
    def __init__(self):
        self.move_list = list()
        self.get_input()

    def get_input(self):
        for i in range(int(input())):
            self.move_list.append(list(input().split()))

    @staticmethod
    def parse_move(move):
        pattern = re.compile('^([a-h])([1-8])([a-h])([1-8])$')
        match = pattern.match(move)
        if match is None:
            raise ValueError("move is invalid")
        # b2b3 = (6,1) (5,1)
        x_from = 8-int(match.group(2))
        y_from = ord(match.group(1))-97
        x_to = 8-int(match.group(4))
        y_to = ord(match.group(3))-97
        return (x_from, y_from), (x_to, y_to)

    def solve(self):
        results = list()
        # iterate though each set of moves
        for moves in self.move_list:
            outcome = 0
            board = ChessBoard()
            for turn, move in enumerate(moves, 1):
                move_from, move_to = self.parse_move(move)  # returns (x1, y1), (x2, y2)
                # check if move is valid and if turn (white/black) is valid
                if board.valid_move(move_from, move_to) and board.valid_turn(move_from, turn):
                    board.move_piece(move_from, move_to)
                    # print("VALID - From: {}, To: {}, Turn: {}".format(move_from, move_to, turn))
                else:
                    # print("INVALID - From: {}, To: {}, Turn: {}".format(move_from, move_to, turn))
                    outcome = turn
                    break
            results.append(str(outcome))
        # end for
        print(" ".join(results))


if __name__ == '__main__':
    Problem76().solve()