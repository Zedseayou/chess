class Move(object):
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
            self.piece = lan[0]
            self.start_square = lan[1:2]
            self.end_square = lan[-2:]
        elif lan[0] in Game.files:
            self.piece = 'P'
            self.start_square = lan[:1]
            self.end_square = lan[-2:]
        else:
            raise ValueError('Invalid long algebraic notation')