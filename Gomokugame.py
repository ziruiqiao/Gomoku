from AI2 import AI

class Gomoku:

    def __init__(self):
        self.y = [[0 for x in range(15)] for y in range(15)]  # present board
        self.cur_step = 0   # step
        self.aic = AI()
        self.S = 0

    def move_1step(self, input_by_window, pos_x, pos_z):
        # player put pieces
        while True:
            try:
                if not input_by_window:
                    pos_x = int(input('x: '))
                    pos_z = int(input('y: '))
                if 0 <= pos_x <= 14 and 0 <= pos_z <= 14:
                    if self.y[pos_z][pos_x] == 0:
                        self.y[pos_z][pos_x] = 1
                        self.cur_step += 1
                        return
            except ValueError:
                continue

    def draw_game(self):
        self.S = 2

    def game_result(self,side):
        empty = 0
        y = self.y
        for eachrow in range(15):
            for eachcol in range(15):
                conti = 1
                try:
                    # continuous 5 on same row
                    if conti and y[eachrow][eachcol] == y[eachrow][eachcol + 1] == y[eachrow][eachcol + 2] == y[eachrow][eachcol + 3] == y[eachrow][eachcol + 4] == side:
                        self.S = side
                        conti -= 1
                except IndexError:
                    continue

                try:
                    # continuous 5 on same column
                    if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol] == y[eachrow + 2][eachcol] == y[eachrow + 3][eachcol] == y[eachrow + 4][eachcol] == side:
                        self.S = side
                        conti -= 1
                except IndexError:
                    pass

                try:
                    # continuous 5 on same declined line
                    if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol + 1] == y[eachrow + 2][eachcol + 2] == y[eachrow + 3][eachcol + 3] == y[eachrow + 4][eachcol + 4] == side:
                        self.S = side
                        conti -= 1
                except IndexError:
                    pass

                try:
                    # continuous 5 on same inclined line
                    if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol - 1] == y[eachrow + 2][eachcol - 2] == y[eachrow + 3][eachcol - 3] == y[eachrow + 4][eachcol - 4] == side:
                        self.S = side
                        conti -= 1
                except IndexError:
                    pass

                if conti:
                    if y[eachrow][eachcol] == 0:
                        empty += 1

        if empty == 0:
            draw_game()
        

    def a_move_1step(self, input_by_window, pos_x, pos_z):
        #self.aic.AIC(self.y)
        # player put pieces
        while True:
            try:
                if not input_by_window:
                    pos_x = int(input('x: '))
                    pos_z = int(input('y: '))
                if 0 <= pos_x <= 14 and 0 <= pos_z <= 14:
                    if self.y[pos_z][pos_x] == 0:
                        self.y[pos_z][pos_x] = -1
                        return
            except ValueError:
                continue

    def ai_move_1step(self):
        self.aic.AIC(self.y)
