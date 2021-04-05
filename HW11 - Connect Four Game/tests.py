import unittest


from Strategy import Service


class Strategy(unittest.TestCase):


    def test_service(self):
        square_size = 100  # the dimension in pixel of a square from the board
        background_colour = (0, 150, 150)  # the color of the background
        circle_colour = (0, 0, 0)  # the color of the circle when is empty
        piece1_colour = (150, 200, 0)  # the color of the piece of first player
        piece2_colour = (200, 0, 0)  # the color of the piece of the second player
        font_winner = (
        "monospace", 85)  # the font when someone wins the game, for the last message, ex:"Congrats, you won!"
        font_title = ("ebrima", 60)  # the font for central message, ex "Welcome to the game"
        font_option = ("calibri", 70)  # the fonr for subtext, ex "player vs player"

        characteristics = [7, 6, square_size, background_colour, circle_colour, piece1_colour,
                           piece2_colour, font_winner, font_title, font_option]

        service = Service(characteristics)
        board = service.board

        service.implement_move(service.board, 1, 1)
        self.assertEqual(service.board[0][0], 0.0)

        self.assertEqual(service.validate_move(3), True)
        service.implement_move(service.board, 2, 1)
        self.assertEqual(service.validate_move(2), True)









