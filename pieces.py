import game

class Piece(object):
    def __init__(self, square, colour):
        """

        Parameters
        ----------
        chessboard
        square
        colour
        """
        self.file = game.Game.files[square[0]]
        self.rank = game.Game.ranks[square[1]]
        self.colour = colour
        self.captured = False

    def move_piece(self, move: game.Move):
        self.file = game.Game.files[move.end_square[0]]
        self.rank = game.Game.ranks[move.end_square[1]]


class King(Piece):
    symbol = 'K'

    def __init__(self, square, colour):
        super().__init__(square, colour)
        if self.colour == 'W':
            self.icon = '♔'
        elif self.colour == 'B':
            self.icon = '♚'
        else:
            raise ValueError("Invalid colour specified! Should be 'W' or 'B'")


class Queen(Piece):
    symbol = 'Q'

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

    def __init__(self, square, colour):
        super().__init__(square, colour)
        if self.colour == 'W':
            self.icon = '♙'
        elif self.colour == 'B':
            self.icon = '♟'
        else:
            raise ValueError("Invalid colour specified! Should be 'W' or 'B'")

