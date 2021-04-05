
import sys
import pygame

"""        
COUNT_COLUMN = 7
COUNT_ROW = 6
SQUARE = 100
BACKGROUND_C = (0, 90, 90)
CIRCLE_C = (200, 40, 50)
PLAYER1_C = (100, 50, 30)
PLAYER2_C = (50, 20, 100)
"""

pygame.init()


class GUI:
    def __init__(self, service, characteristics):
        self.__service = service
        self.__count_column = characteristics[0]
        self.__count_row = characteristics[1]
        self.__square = characteristics[2]
        self.__background_c = characteristics[3]
        self.__circle_c = characteristics[4]
        self.__piece1_c = characteristics[5]
        self.__piece2_c = characteristics[6]
        self.__font_win = pygame.font.SysFont(characteristics[7][0], characteristics[7][1])
        self.__font_title = pygame.font.SysFont(characteristics[8][0], characteristics[8][1])
        self.__font_option = pygame.font.SysFont(characteristics[9][0], characteristics[9][1])
        self.board = self.__service.board
        self.window = self.__service.window



    def draw_board(self, surface, board):
        """
        - first it draws the "form" of the board, it draws the empty circles
        - it fills the circle with the specific color: if 1 -> player 1 -> color 1
                                                       if 2 -> player 2/computer -> color 2
        """
        radius = int(self.__square / 2) - 5
        height = int((self.__count_row + 1) * self.__square)
        size = (self.__square, self.__square)

        for r in range(self.__count_row):
            for c in range(self.__count_column):
                # rectangle
                position = (c * self.__square, r * self.__square + self.__square)
                pygame.draw.rect(surface, self.__background_c, (position, size))
                # circle
                position = (c * self.__square + radius + 5, (r * self.__square + self.__square + radius + 5))
                pygame.draw.circle(surface, self.__circle_c, position, radius)

        for c in range(self.__count_column):
            for r in range(self.__count_row):

                position = (c * self.__square + radius + 5, height - (r * self.__square + radius + 5))
                if board[r][c] == 1:
                    pygame.draw.circle(surface, self.__piece1_c, position, radius)
                elif board[r][c] == 2:
                    pygame.draw.circle(surface, self.__piece2_c, position, radius)

        pygame.display.update()

    def draw_start_board(self):
        start_label = self.__font_title.render("Welcome to the game!", True, (0, 100, 0))
        two_players_label = self.__font_option.render("Player vs Player", True, (0, 0, 0), (0, 100, 0))
        one_player_label = self.__font_option.render("Player vs Computer", True, (0, 0, 0), (0, 100, 0))
        while True:
            pygame.draw.rect(self.window, self.__background_c, (
                (0, 0), (self.__count_column * self.__square, int((self.__count_row + 1) * self.__square))))
            self.window.blit(start_label, (55, 0))
            self.window.blit(two_players_label, (100, 200))
            self.window.blit(one_player_label, (100, 400))
            pygame.display.update()

            option = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = int(event.pos[0])
                    posy = int(event.pos[1])
                    if posx in range(100, 535) and posy in range(200, 270):
                        option = 1
                    elif posx in range(100, 645) and posy in range(400, 470):
                        option = 2

            if option != 0:
                pygame.time.wait(1000)
                return option

    def run_gui(self):
        game_mode = self.draw_start_board()
        stop_the_game = False
        turn = 0  # turn 0 for player1 and turn 1 for player2/computer
        self.draw_board(self.window, self.board)

        while not stop_the_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEMOTION:
                    self.__service.move_mouse(event.pos[0], turn)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == 0:
                        if self.__service.move_player(event.pos[0], 1) == 0:
                            turn = turn - 1  # it checks if the move was valid and dec turn with 1, in order not to
                            # change the turn so the player move will not be consumed
                        else:
                            self.draw_board(self.window, self.board)

                        if self.__service.check_win(1):
                            label = self.__font_win.render("Player 1 wins!", True, self.__piece1_c, (0, 0, 0))
                            self.window.blit(label, (0, 0))
                            pygame.display.update()

                            stop_the_game = True

                    elif game_mode == 1:
                        # player two round
                        if self.__service.move_player(event.pos[0], 2) == 0:
                            turn = turn - 1  # it checks if the move was valid and dec turn with 1, in order not to
                            # change the turn so the player move will not be consumed

                        if self.__service.check_win(2):
                            label = self.__font_win.render("Player 2 wins!", True, self.__piece2_c, (0, 0, 0))
                            self.window.blit(label, (0, 0))
                            pygame.display.update()
                            stop_the_game = True

                    turn = turn + 1
                    turn = turn % 2

                elif game_mode == 2 and turn == 1 and not stop_the_game:
                    # Computer move:
                    pygame.time.wait(200)
                    if self.__service.move_computer() == 0:
                        turn = turn - 1
                    else:
                        self.draw_board(self.window, self.board)
                    if self.__service.check_win(2):
                        label = self.__font_win.render("Computer wins! ", True, self.__piece2_c, (0, 0, 0))
                        self.window.blit(label, (0, 0))
                        pygame.display.update()
                        stop_the_game = True

                    turn = turn + 1
                    turn = turn % 2

                if stop_the_game:
                    pygame.time.wait(4000)
