import chess


class Game(object):

    def __init__(self):
        self.board = [['\u2001'] * 8 for _ in range(8)]
        self.turn = 1
        self.player = "White"
        self.piece_list = []

    def new_game(self):
        self.turn = 1
        self.player = "White"

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


