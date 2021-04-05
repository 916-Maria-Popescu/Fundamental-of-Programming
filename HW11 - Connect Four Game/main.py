import numpy as np
from ConsoleUI import Console
from GUI import GUI
from Strategy import Service
import pygame

if __name__ == '__main__':

    option = 'GUI'                 # \ UI or GUI

    count_column = 7               # number of columns
    count_row = 6                  # number of rows
    board = np.zeros((count_row, count_column))

    square_size = 100              # the dimension in pixel of a square from the board
    background_colour = (0, 150, 150)  # the color of the background
    circle_colour = (0, 0, 0)  # the color of the circle when is empty
    piece1_colour = (150, 200, 0)    # the color of the piece of first player
    piece2_colour = (200, 0, 0)    # the color of the piece of the second player
    font_winner = ("monospace", 85) # the font when someone wins the game, for the last message, ex:"Congrats, you won!"
    font_title = ("ebrima", 60)   # the font for central message, ex "Welcome to the game"
    font_option = ("calibri", 70)  # the fonr for subtext, ex "player vs player"

    characteristics = [count_column, count_row, square_size, background_colour, circle_colour, piece1_colour,
                       piece2_colour, font_winner, font_title, font_option]

    if option == 'UI':

        service = Service(characteristics)
        console = Console(service)

        console.run_console()

    elif option == 'GUI':
        service = Service(characteristics)
        console = GUI(service, characteristics)
        print(pygame.font.get_fonts())

        console.run_gui()

