import unittest
import chess


class TestMove(unittest.TestCase):

    def test_capture(self):
        self.assertTrue(game.Move("Ne1xf3").capture)
        self.assertTrue(game.Move("e4xd5").capture)
        self.assertFalse(game.Move("Ne1-f3").capture)
        self.assertFalse(game.Move("e4-d5").capture)

    def test_piece(self):
        self.assertTrue(game.Move("Ne1xf3").piece == 'N')
        self.assertTrue(game.Move("e4xd5").piece == 'P')
        self.assertTrue(game.Move("Ke1xf2").piece == 'K')
        self.assertTrue(game.Move("Qc4xd5").piece == 'Q')
        self.assertTrue(game.Move("Be1xf2").piece == 'B')
        self.assertTrue(game.Move("Rh1-h7").piece == 'R')

        with self.assertRaises(ValueError):
            game.Move("Xe1xf3")




# class TestPieces(unittest.TestCase)


if __name__ == '__main__':
    unittest.main()