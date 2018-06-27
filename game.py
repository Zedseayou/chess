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
        self.board = [['\u2001'] * 8 for _ in range(8)]
        self.turn = 1
        self.player = "White"
        self.piece_list = []

    def __repr__(self):
        top = '┌\u3000┬\u3000┬\u3000┬\u3000┬\u3000┬\u3000┬\u3000┬\u3000┐'
        centre = '├\u3000┼\u3000┼\u3000┼\u3000┼\u3000┼\u3000┼\u3000┼\u3000┤'
        bottom = '└\u3000┴\u3000┴\u3000┴\u3000┴\u3000┴\u3000┴\u3000┴\u3000┘'

        rows = [' '.join(row) for row in self.board]
        printed_board = f'{top}\n' + \
            f' {rows[0]} \n' + \
            f'{centre}\n' + \
            f' {rows[1]} \n' + \
            f'{centre}\n' + \
            f' {rows[2]} \n' + \
            f'{centre}\n' + \
            f' {rows[3]} \n' + \
            f'{centre}\n' + \
            f' {rows[4]} \n' + \
            f'{centre}\n' + \
            f' {rows[5]} \n' + \
            f'{centre}\n' + \
            f' {rows[6]} \n' + \
            f'{centre}\n' + \
            f' {rows[7]} \n' + \
            f'{bottom}'
        return printed_board

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

    def new_game(self):
        self.turn = 1
        self.player = "White"
        self.piece_list = []

        for square in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']:
            self.add_piece('P', square, 'W')
        for square in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
            self.add_piece('P', square, 'B')
        for square in ['a1', 'h1']:
            self.add_piece('R', square, 'W')
        for square in ['a8', 'h8']:
            self.add_piece('R', square, 'B')
        for square in ['b1', 'g1']:
            self.add_piece('N', square, 'W')
        for square in ['b8', 'g8']:
            self.add_piece('N', square, 'B')
        for square in ['c1', 'f1']:
            self.add_piece('B', square, 'W')
        for square in ['c8', 'f8']:
            self.add_piece('B', square, 'B')
        self.add_piece('Q', 'd1', 'W')
        self.add_piece('Q', 'd8', 'B')
        self.add_piece('K', 'e1', 'W')
        self.add_piece('K', 'e8', 'B')

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