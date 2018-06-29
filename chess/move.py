import chess


class Move(object):
    """

    Attributes
    ----------
    capture : bool
    piece_symbol : str
    start_square:
    end_square:

    """
    def __init__(self, lan):
        """Create a move object.

        Move objects wrap the parsing of move notation

        Parameters
        ----------
        lan : str
            The long algebraic notation for the move. This looks like e2-e4 or Nb1xc3.
        """

        if lan.find('x') != -1:
            self.capture = True
        else:
            self.capture = False

        if lan[0] in ['K', 'Q', 'B', 'N', 'R']:
            self.piece_symbol = lan[0]
            self.start_square = lan[1:3]
            self.end_square = lan[-2:]
        elif lan[0] in chess.Board.files:
            self.piece_symbol = 'P'
            self.start_square = lan[:2]
            self.end_square = lan[-2:]
        else:
            raise ValueError('Invalid long algebraic notation')

        self.start_indices = chess.Board.n2i(self.start_square)
        self.end_indices = chess.Board.n2i(self.end_square)

    def __repr__(self):
        display = f'{chess.pieces.Piece.piece_names[self.piece_symbol]} from {self.start_square} to {self.end_square}'
        return display