import copy
import math
import random

import numpy as np
import pygame


class Service:
    def __init__(self, characteristics):
        self.__count_column = characteristics[0]
        self.__count_row = characteristics[1]
        self.__square = characteristics[2]
        self.__background_c = characteristics[3]
        self.__circle_c = characteristics[4]
        self.__piece1_c = characteristics[5]
        self.__piece2_c = characteristics[6]
        self.board = np.zeros((self.__count_row, self.__count_column))
        self.width = self.__count_column * self.__square
        self.height = int((self.__count_row + 1) * self.__square)
        self.window = pygame.display.set_mode((self.width, self.height))

    def validate_move(self, column):
        """
        Checks if the last row ( for the given column) is empty(0)
        """
        return self.board[self.__count_row - 1][column] == 0

    def implement_move(self, board, column, piece):
        """
        Finds the next empty spot on the given column, and transform it in piece (1 for player 1, 2 for player2)
        """
        for r in range(self.__count_row):
            if board[r][column] == 0:
                board[r][column] = piece
                break

    def flip_board(self):
        return np.flip(self.board, 0)

    def check_win(self, piece):
        """
        Check if there are 4 pieces next to each other on a vertical, horizontal or diagonal position:

        -> vertical: 0         -> horizontal: 0 0 0 0
                     0
                     0
                     0

                         0                    0
        -> diagonal up: 0      diagonal down:  0
                       0                        0
                      0                          0
        """
        # vertical
        for column in range(self.__count_column):
            for row in range(self.__count_row - 3):
                if self.board[row][column] == piece and self.board[row + 1][column] == piece and self.board[row + 2][
                    column] == piece and \
                        self.board[row + 3][column] == piece:
                    return True

        # horizontal
        for column in range(self.__count_column - 3):
            for row in range(self.__count_row):
                if self.board[row][column] == piece and self.board[row][column + 1] == piece and self.board[row][
                    column + 2] == piece and \
                        self.board[row][column + 3] == piece:
                    return True

        # diagonal_up
        for column in range(self.__count_column - 3):
            for row in range(self.__count_row - 3):
                if self.board[row][column] == piece and self.board[row + 1][column + 1] == piece and \
                        self.board[row + 2][column + 2] == piece and self.board[row + 3][column + 3] == piece:
                    return True

        # diagonal_down
        for column in range(self.__count_column - 3):
            for row in range(self.__count_row - 3, self.__count_row):
                if self.board[row][column] == piece and self.board[row - 1][column + 1] == piece and \
                        self.board[row - 2][column + 2] == piece and self.board[row - 3][column + 3] == piece:
                    return True


    def move_mouse(self, posx, turn):
        """
        when the mouse will move, it will show the piece in the color of that player
        """
        pygame.draw.rect(self.window, (0, 0, 0), (0, 0, self.width, self.__square))
        radius = int(self.__square / 2)
        if turn == 0:
            pygame.draw.circle(self.window, self.__piece1_c, (posx, radius), radius)

        else:
            pygame.draw.circle(self.window, self.__piece2_c, (posx, radius), radius)
        pygame.display.update()

    def move_player(self, posx, piece):
        """
        Takes the position of the mouse when it was clicked and it converts in a number from 1 to 7
        That number will be the column the player choose to drop the piece
        It validates the move, if it is valid, it returns it, otherwise 0
        """
        move = int(math.floor(posx / self.__square))
        if self.validate_move(move):
            self.implement_move(self.board, move, int(piece))
        else:
            return 0

    def move_computer(self):
        """
        Choose a move for the computer to make
        """
        move = self.pick_best_move_computer(2)
        # move = int(self.choose_move_computer())
        if self.validate_move(move):
            self.implement_move(self.board, move, 2)
        else:
            return 0

    def pick_best_move_computer(self, piece):
        """
        It simulates a move on an new board (copied from the original one) in order to calculate the score for that
        move
        It choose the best score and take de corespondent coloumn as the next move
        """
        possible_choices = []

        for column in range(self.__count_column):
            if self.validate_move(column):
                possible_choices.append(column)

        best_move = random.choice(possible_choices)
        best_score = -300  # set the score so that it will find a better score
        for column in possible_choices:
            auxiliar_board = copy.deepcopy(self.board)
            self.implement_move(auxiliar_board, column, piece)
            score = self.all_score_possibilites(auxiliar_board, piece)

            if score > best_score:
                best_score = score
                best_move = column

        return best_move

    def all_score_possibilites(self, board, piece):
        """
        For all the possible circles, it takes all the possible extension that would  form a line (4 circles in
        diagonal, horizontal, vertical) and sum up the score
        """
        score = 0
        # central column:
        central_array = [int(i) for i in list(board[:, self.__count_column // 2])]
        score = score + central_array.count(piece) * 2

        # for vertical lines
        for column in range(self.__count_column):
            column_array = [int(i) for i in list(board[:, column])]
            for row in range(self.__count_row - 3):
                extension = column_array[row:row + 4]
                score = score + self.score_extension(extension, piece)

        # for horizontal lines
        for row in range(self.__count_row):
            row_array = [int(i) for i in list(board[row, :])]
            for column in range(self.__count_column - 3):
                extension = row_array[column:column + 4]
                score = score + self.score_extension(extension, piece)

        # for diagonals
        for row in range(self.__count_row - 3):
            for column in range(self.__count_column - 3):
                extension = [board[row + i][row + i] for i in range(4)]
                score = score + self.score_extension(extension, piece)

        for row in range(self.__count_row - 3):
            for column in range(self.__count_column - 3):
                extension = [board[row - i + 3][column + i] for i in range(4)]
                score = score + self.score_extension(extension, piece)

        return score

    def score_extension(self, extension, piece):
        """
        Calculates the score for a piece put in a new position
        The scores are made so that the best position gets the best score
        -win the game
        -block the winning move of the other player
        -put 3 pieces in a window (diagonal, horizontal, verticaL)
        -put 2 pieces in a window
        """
        score = 0
        other_piece = 1
        if piece == 1:  # player
            other_piece = 2  # computer

        if extension.count(piece) == 4:
            score = score + 300
        elif extension.count(piece) == 3 and extension.count(0) == 1:
            score = score + 70
        elif extension.count(piece) == 2 and extension.count(0) == 2:
            score = score + 20
        if extension.count(other_piece) == 3 and extension.count(0) == 1:
            score = score - 100

        return score
