import chess


class Board(object):

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
        self.layout = [['\u2001'] * 8 for _ in range(8)]
        self.piece_list = []

    def __repr__(self):
        top = '┌' + '\u2005\u3000\u2005┬' * 7 + '\u2005\u3000\u2005┐'
        centre = '├' + '\u2005\u3000\u2005┼' * 7 + '\u2005\u3000\u2005┤'
        bottom = '└' + '\u2005\u3000\u2005┴' * 7 + '\u2005\u3000\u2005┘'

        rows = ['\u2005 \u2005'.join(row) for row in self.layout]
        representation: str = f'{top}\n' + \
                              f'\u2005 {rows[0]} \u2005\n' + \
                              f'{centre}\n' + \
                              f'\u2005 {rows[1]} \u2005\n' + \
                              f'{centre}\n' + \
                              f'\u2005 {rows[2]} \u2005\n' + \
                              f'{centre}\n' + \
                              f'\u2005 {rows[3]} \u2005\n' + \
                              f'{centre}\n' + \
                              f'\u2005 {rows[4]} \u2005\n' + \
                              f'{centre}\n' + \
                              f'\u2005 {rows[5]} \u2005\n' + \
                              f'{centre}\n' + \
                              f'\u2005 {rows[6]} \u2005\n' + \
                              f'{centre}\n' + \
                              f'\u2005 {rows[7]} \u2005\n' + \
                              f'{bottom}'
        return representation

    @staticmethod
    def n2i(square):
        file = Board.files[square[0]]
        rank = Board.ranks[square[1]]
        return rank, file

    @staticmethod
    def i2n(rank, file):
        inv_files = {v: k for k, v in Board.files.items()}
        inv_ranks = {v: k for k, v in Board.ranks.items()}
        square = inv_ranks[rank] + inv_files[file]
        return square

    def add_piece(self, piece_type, square, colour):
        """Add a piece to the board.

        This adds

        Parameters
        ----------
        piece_type : str
            One of K, Q, R, B, N, P
        square : str
            Two-character string specifying the square
        colour : str
            Either 'W' or 'B'

        Returns
        -------

        """
        if piece_type == 'K':
            new_piece = pieces.King(square, colour)
        elif piece_type == 'Q':
            new_piece = pieces.Queen(square, colour)
        elif piece_type == 'R':
            new_piece = pieces.Rook(square, colour)
        elif piece_type == 'B':
            new_piece = pieces.Bishop(square, colour)
        elif piece_type == 'N':
            new_piece = pieces.Knight(square, colour)
        elif piece_type == 'P':
            new_piece = pieces.Pawn(square, colour)
        else:
            raise ValueError('Invalid piece_type! Should be one of K, Q, R, B, N, P')

        self.piece_list.append(new_piece)
        self.layout[new_piece.rank][new_piece.file] = new_piece.icon

    def start_position(self):
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