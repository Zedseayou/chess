import pieces

class Game(object):

    ranks = {
        '8': 0,
        '7': 1,
        '6': 2,
        '5': 3,
        '4': 4,
        '3': 5,
        '2': 6,
        '1': 7
    }

    files = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }

    def __init__(self):
        self.board = [[''] * 8 for _ in range(8)]
        self.turn = "White"
        self.piece_list = []

    def add_piece(self, type, square, colour):
        """Add a piece to the board.



        Parameters
        ----------
        type : str
            One of K, Q, R, B, N, P
        square : str
            Two-character string specifying the square
        colour : str
            Either 'W' or 'B'

        Returns
        -------

        """
        if type == 'K':
            new_piece = pieces.King(square, colour)
        elif type == 'Q':
            new_piece = pieces.Queen(square, colour)
        elif type == 'R':
            new_piece = pieces.Rook(square, colour)
        elif type == 'B':
            new_piece = pieces.Bishop(square, colour)
        elif type == 'N':
            new_piece = pieces.Knight(square, colour)
        elif type == 'P':
            new_piece = pieces.Pawn(square, colour)
        else:
            raise ValueError('Invalid piece type! Should be one of K, Q, R, B, N, P')

        self.piece_list.append(new_piece)
        self.board[new_piece.rank][new_piece.file] = new_piece.icon

    # def remove_piece(self, square):


    # def setup(self):



    # def make_move(self):
    #     command = input('Enter your move in long algebraic notation:')
    #     move = Move(command)
    #
    #
    #
    #
    #     self.board[self.ranks[move.start_square[0]]][self.files[move.start_square[1]]]
    #
    #     return move.piece


class Move(object):
    def __init__(self, lan):
        """Create a move object

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
            self.piece = lan[0]
            self.start_square = lan[1:2]
            self.end_square = lan[-2:]
        elif lan[0] in Game.files:
            self.piece = 'P'
            self.start_square = lan[:1]
            self.end_square = lan[-2:]
        else:
            raise ValueError('Invalid long algebraic notation')