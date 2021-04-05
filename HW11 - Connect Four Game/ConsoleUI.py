import random

"""
 Connect Four is a two-player connection board game, in which the players choose a color and then take turns dropping
 colored discs into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the
 lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical,
 or diagonal line of four of one's own discs.
"""


class Console:
    def __init__(self, service):
        self.__service = service

    def run_console(self):

        # ---------------------------------------------------------Options
        print("Welcome to the game")
        option = input("How do you want to play?\n"
                       " 1 -> player vs player\n"
                       " 2 -> Player vs computer\n"
                       " my option:")
        name1 = input("Player 1, please enter your name: ")

        if option == '1':
            # Player versus player game:
            name2 = input("Player 2, please enter your name: ")
            print(name1, " and ", name2, "you'll play against each other")

        elif option == '2':
            # Player versus computer game:
            print(name1, "you'll play against the Computer")
            name2 = 'Computer'
        else:
            print("sorry! wrong option!")

        print(self.__service.flip_board())

        # ------------------------------------------------------------------SetUp
        stop_the_game = False
        turn = 0  # turn 0 for player1 and turn 1 for player2/computer
        # --------------------------------------------------------------------the game
        while stop_the_game is False:
            if turn == 0:

                # Player 1 move:

                piece = 1
                while True:
                    move = int(input(name1 + ", what column do you choose? : ")) - 1
                    if self.__service.validate_move(move):
                        self.__service.implement_move(move, piece)
                        print(self.__service.flip_board())
                        break
                    else:
                        print("That column is already full!")
                if self.__service.check_win(piece):
                    stop_the_game = True
                    print("Congrats!!!", name1, "you are the winner!")

            else:
                piece = 2
                # Player 2 or Computer

                if option == '1':

                    # Player 2 move:

                    while True:
                        move = int(input(name2 + ", what column do you choose? : ")) - 1
                        if self.__service.validate_move(move):
                            self.__service.implement_move(move, piece)
                            print(self.__service.flip_board())
                            break
                        else:
                            print("That column is already full!")

                    if self.__service.check_win(piece):
                        stop_the_game = True
                        print("Congrats!!!", name2, "you are the winner!")

                else:

                    # Computer move:

                    while True:
                        move = random.randint(0, 6)
                        if self.__service.validate_move(move):
                            self.__service.implement_move(move, piece)
                            print("Computer move: ", move + 1)
                            print(self.__service.flip_board())
                            break
                    if self.__service.check_win(piece):
                        stop_the_game = True
                        print(name1, "you are the loser!")

            turn = turn + 1
            turn = turn % 2
