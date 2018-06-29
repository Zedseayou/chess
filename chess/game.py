import chess


class Game(object):

    def __init__(self):
        self.board = chess.Board()
        self.turn = 1
        self.player = "White"
        self.piece_list = []
        self.move_history = []

    def __repr__(self):
        display = f'Turn {self.turn}, {self.player} to play.\n' + repr(self.board)
        return display

    def new_game(self):
        self.turn = 1
        self.player = "White"
        self.board.start_position()

    def make_move(self):
        command = input('Enter your move in long algebraic notation:')
        move = chess.Move(command)
        self.board.move_piece(move)




        self.board[self.ranks[move.start_square[0]]][self.files[move.start_square[1]]]

        return move.piece


