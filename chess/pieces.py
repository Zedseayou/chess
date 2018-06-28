import chess


class Piece(object):

    def __init__(self, square, colour):
        """

        Parameters
        ----------
        square
        colour
        """
        self.square = square
        self.file = board.Board.n2i(square)[1]
        self.rank = board.Board.n2i(square)[0]
        self.colour = colour
        self.captured = False

    def __repr__(self):
        if self.captured:
            description = f'Captured {self.name}'
        else:
            description = f'{self.name} at {self.square}'
        return description

    def move_piece(self, move):
        self.square = move.end_square
        self.file = game.Game.files[move.end_square[0]]
        self.rank = game.Game.ranks[move.end_square[1]]


class King(Piece):
    symbol = 'K'
    name = 'King'

    def __init__(self, square, colour):
        super().__init__(square, colour)
        if self.colour == 'W':
            self.icon = '♔'
        elif self.colour == 'B':
            self.icon = '♚'
        else:
            raise ValueError("Invalid colour specified! Should be 'W' or 'B'")

    def legal_moves(self):
        neighbours = set(itertools.product(
            [self.rank, self.rank - 1, self.rank + 1],
            [self.file, self.file - 1, self.file + 1]
        )) - set((self.rank, self.file))
        squares = [

        ]

class Queen(Piece):
    symbol = 'Q'
    name = 'Queen'

    def __init__(self, square, colour):
        super().__init__(square, colour)
        if self.colour == 'W':
            self.icon = '♕'
        elif self.colour == 'B':
            self.icon = '♛'
        else:
            raise ValueError("Invalid colour specified! Should be 'W' or 'B'")


class Rook(Piece):
    symbol = 'R'
    name = 'Rook'

    def __init__(self, square, colour):
        super().__init__(square, colour)
        if self.colour == 'W':
            self.icon = '♖'
        elif self.colour == 'B':
            self.icon = '♜'
        else:
            raise ValueError("Invalid colour specified! Should be 'W' or 'B'")


class Bishop(Piece):
    symbol = 'B'
    name = 'Bishop'

    def __init__(self, square, colour):
        super().__init__(square, colour)
        if self.colour == 'W':
            self.icon = '♗'
        elif self.colour == 'B':
            self.icon = '♝'
        else:
            raise ValueError("Invalid colour specified! Should be 'W' or 'B'")


class Knight(Piece):
    symbol = 'N'
    name = 'Knight'

    def __init__(self, square, colour):
        super().__init__(square, colour)
        if self.colour == 'W':
            self.icon = '♘'
        elif self.colour == 'B':
            self.icon = '♞'
        else:
            raise ValueError("Invalid colour specified! Should be 'W' or 'B'")


class Pawn(Piece):
    symbol = 'P'
    name = 'Pawn'

    def __init__(self, square, colour):
        super().__init__(square, colour)
        if self.colour == 'W':
            self.icon = '♙'
        elif self.colour == 'B':
            self.icon = '♟'
        else:
            raise ValueError("Invalid colour specified! Should be 'W' or 'B'")

