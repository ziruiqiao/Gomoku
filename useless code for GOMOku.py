    def winning(Win,side,y):
        # Winning conditions
        def win_action(side):
            if side == 1:
                print('You Win !!')
            else:
                print('You Lose ')
            # exit the game
        if Win:
            win_action(side)
        else:
            for eachrow in range(15):
                for eachcol in range(15):
                    conti = True
                    try:
                        # continuous 5 on same row
                        if conti and y[eachrow][eachcol] == y[eachrow][eachcol + 1] == y[eachrow][eachcol + 2] == y[eachrow][eachcol + 3] == y[eachrow][eachcol + 4] == 1:
                            win_action(side)
                            conti = False
                    except IndexError:
                        pass

                    try:
                        # continuous 5 on same column
                        if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol] == y[eachrow + 2][eachcol] == y[eachrow + 3][eachcol] == y[eachrow + 4][eachcol] == 1:
                            win_action(side)
                            conti = False
                    except IndexError:
                        pass

                    try:
                        # continuous 5 on same declined line
                        if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol + 1] == y[eachrow + 2][eachcol + 2] == y[eachrow + 3][eachcol + 3] == y[eachrow + 4][eachcol + 4] == 1:
                            win_action(side)
                            conti = False
                    except IndexError:
                        pass

                    try:
                        # continuous 5 on same inclined line
                        if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol - 1] == y[eachrow + 2][eachcol - 2] == y[eachrow + 3][eachcol - 3] == y[eachrow + 4][eachcol - 4] == 1:
                            win_action(side)
                            conti = False
                    except IndexError:
                        pass
                    try:
                        # continuous 4 on same row with two sides clear
                        if conti and y[eachrow][eachcol] == y[eachrow][eachcol + 1] == y[eachrow][eachcol + 2] == y[eachrow][eachcol + 3] == side:
                            if y[eachrow][eachcol - 1] == y[eachrow][eachcol + 4] == -side:
                                win_action(side)
                                conti = False
                    except IndexError:
                        pass
                    try:
                        # continuous 4 on same column with two sides clear
                        if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol] == y[eachrow + 2][eachcol] == y[eachrow + 3][eachcol] == side:
                            if y[eachrow - 1][eachcol] == y[eachrow + 4][eachcol] == -side:
                                win_action(side)
                                conti = False
                    except IndexError:
                        pass
                    try:
                        # continuous 4 on same declined line with two sides clear
                        if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol + 1] == y[eachrow + 2][eachcol + 2] == y[eachrow + 3][eachcol + 3] == side:
                            if y[eachrow - 1][eachcol - 1] == -side or y[eachrow + 4][eachcol + 4] == -side:
                                win_action(side)
                                conti = False
                    except IndexError:
                        pass
                    try:
                        # continuous 4 on same inclined line with two sides clear
                        if conti and y[eachrow][eachcol] == y[eachrow + 1][eachcol - 1] == y[eachrow + 2][eachcol - 2] == y[eachrow + 3][eachcol - 3] == side:
                            if y[eachrow - 1][eachcol + 1] == y[eachrow + 4][eachcol - 4] == -side:
                                win_action(side)
                                conti = False
                    except IndexError:
                        pass



    def show(self, res):
        """显示游戏内容"""
        for y in range(15):
            for x in range(15):
                if self.y[z][x] == 0:
                    print('  ', end='')
                elif self.g_map[x][y] == 1:
                    print('〇', end='')
                elif self.g_map[x][y] == -1:
                    print('×', end='')

                if x != 14:
                    print('-', end='')
            print('\n', end='')
            for x in range(15):
                print('|  ', end='')
            print('\n', end='')

        if res == 1:
            print('玩家获胜!')
        elif res == 2:
            print('电脑获胜!')
        elif res == 3:
            print('平局!')

    def play(self):
        while True:
            self.move_1step()  
            res = self.game_result()  
            if res != 0: 
                self.show(res)
                return
            self.ai_move_1step()  
            res = self.game_result()
            if res != 0:
                self.show(res)
                return
            self.show(0)  

