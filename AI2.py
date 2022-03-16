import random as r

class AI:
    def __init__(self):
        self.result = []
        self.five = 0
        self.four = 0
        self.three = 0
        self.two = 0
    def row_test(self, num, x, z, y, side):
        if num == 5:
            if 0 <= x <= 10:
                #oooox
                if y[z][x] == y[z][x + 1] == y[z][x + 2] == y[z][x + 3] == side and y[z][x + 4] == 0:
                    self.five += 1
                    return '%d,%d' % (z, (x + 4))
                #oooxo
                elif y[z][x] == y[z][x + 1] == y[z][x + 2] == y[z][x + 4] == side and y[z][x + 3] == 0:
                    self.five += 1
                    return '%d,%d' % (z, (x + 3))
                #ooxoo
                elif y[z][x] == y[z][x + 1] == y[z][x + 3] == y[z][x + 4] == side and y[z][x + 2] == 0:
                    self.five += 1
                    return '%d,%d' % (z, (x + 2))
                #oxooo
                elif y[z][x] == y[z][x + 2] == y[z][x + 3] == y[z][x + 4] == side and y[z][x + 1] == 0:
                    self.five += 1
                    return '%d,%d' % (z, (x + 1))
                #xoooo
                elif y[z][x + 1] == y[z][x + 2] == y[z][x + 3] == y[z][x + 4] == side and y[z][x] == 0:
                    self.five += 1
                    return '%d,%d' % (z, x)

        if num == 4:
            if 0 <= x <= 9:
                #xxooox
                if y[z][x + 2] == y[z][x + 3] == y[z][x + 4] == side and y[z][x + 5] == y[z][x + 1] == 0:
                    if y[z][x] == 0:
                        self.four += 1
                        return '%d,%d' % (z, (x + 1))
                #xoooxx
                elif y[z][x + 1] == y[z][x + 2] == y[z][x + 3] == side and y[z][x + 4] == y[z][x] == 0:
                    if y[z][x + 5] == 0:
                        self.four += 1
                        return '%d,%d' % (z, (x + 4))

            if 0 <= x <= 10:
                #ooxox
                if y[z][x] == y[z][x + 1] == y[z][x + 3] == side and y[z][x + 2] == y[z][x + 4] == 0:
                    self.four += 1
                    return '%d,%d' % (z, (x + 2))
                #oxoox
                elif y[z][x] == y[z][x + 2] == y[z][x + 3] == side and y[z][x + 1] == y[z][x + 4] == 0:
                    self.four += 1
                    return '%d,%d' % (z, (x + 1))
                #xooxo
                elif y[z][x + 1] == y[z][x + 2] == y[z][x + 4] == side and y[z][x] == y[z][x + 3] == 0:
                    self.four += 1
                    return '%d,%d' % (z, (x + 3))
                #xoxoo
                elif y[z][x + 1] == y[z][x + 3] == y[z][x + 4] == side and y[z][x] == y[z][x + 2] == 0:
                    self.four += 1
                    return '%d,%d' % (z, (x + 2))


        if num == 3:
            if 0 <= x <= 11:
                #ooox
                if y[z][x] == y[z][x + 1] == y[z][x + 2] == side and y[z][x + 3] == 0:
                    self.three += 1
                    return '%d,%d' % (z, (x + 3))
                #xooo
                elif y[z][x + 1] == y[z][x + 2] == y[z][x + 3] == side and y[z][x] == 0:
                    self.three += 1
                    return '%d,%d' % (z, x)
                #xoox
                elif y[z][x + 1] == y[z][x + 2] == side and y[z][x + 3] == y[z][x] == 0:
                    self.three += 1
                    return  '%d,%d' % (z, x)
                #oxox
                elif y[z][x] == y[z][x + 2] == side and y[z][x + 1] == y[z][x + 3] == 0:
                    self.three += 1
                    return  '%d,%d' % (z, (x + 1))
                #xoxo
                elif y[z][x + 1] == y[z][x + 3] == side and y[z][x] == y[z][x + 2] == 0:
                    self.three += 1
                    return  '%d,%d' % (z, (x + 2))

    def col_test(self, num, x, z, y, side):
        if num == 5:
            if 0 <= z <= 10:
                if y[z][x] == y[z + 1][x] == y[z + 2][x] == y[z + 3][x] == side and y[z + 4][x] == 0:
                        self.five += 1
                        return '%d,%d' % ((z + 4), x)
                elif y[z][x] == y[z + 1][x] == y[z + 2][x] == y[z + 4][x] == side and y[z + 3][x] == 0:
                        self.five += 1
                        return '%d,%d' % ((z + 3), x)
                elif y[z][x] == y[z + 1][x] == y[z + 3][x] == y[z + 4][x] == side and y[z + 2][x] == 0:
                        self.five += 1
                        return '%d,%d' % ((z + 2), x)
                elif y[z][x] == y[z + 2][x] == y[z + 3][x] == y[z + 4][x] == side and y[z + 1][x] == 0:
                        self.five += 1
                        return '%d,%d' % ((z + 1), x)
                elif y[z + 1][x] == y[z + 2][x] == y[z + 3][x] == y[z + 4][x] == side and y[z][x] == 0:
                        self.five += 1
                        return '%d,%d' % (z, x)

        if num == 4:
            if 0 <= z <= 9:
                if y[z + 2][x] == y[z + 3][x] == y[z + 4][x] == side and y[z + 1][x] == y[z + 5][x] == 0:
                    if y[z][x] == 0:
                        self.four += 1
                        return '%d,%d' % ((z + 1), x)
                elif y[z + 1][x] == y[z + 2][x] == y[z + 3][x] == side and y[z][x] == y[z + 4][x] == 0:
                    if y[z + 5][x]:
                        self.four += 1
                        return '%d,%d' % ((z + 4), x)
            if 0 <= z <= 10:
                if y[z + 1][x] == y[z + 2][x] == y[z + 4][x] == side and y[z + 3][x] == y[z][x] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 3), x)
                elif y[z + 1][x] == y[z + 3][x] == y[z + 4][x] == side and y[z + 2][x] == y[z][x] ==  0:
                    self.four += 1
                    return '%d,%d' % ((z + 2), x)
                elif y[z][x] == y[z + 1][x] == y[z + 3][x] == side and y[z + 2][x] == y[z + 4][x] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 2), x)
                elif y[z][x] == y[z + 2][x] == y[z + 3][x] == side and y[z + 1][x] == y[z + 4][x] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 1), x)


        if num == 3:
            if 0 <= z <= 11:
                if y[z][x] == y[z + 1][x] == y[z + 2][x] == side and y[z + 3][x] == 0:
                    self.three += 1
                    return '%d,%d' % ((z + 3), x)
                elif y[z + 1][x] == y[z + 2][x] == y[z + 3][x] == side and y[z][x] == 0:
                    self.three += 1
                    return '%d,%d' % (z, x)
                elif y[z][x] == y[z + 2][x] == side and y[z + 1][x] == y[z + 3][x] == 0:
                    self.three += 1
                    return '%d,%d' % ((z + 1), x)
                elif y[z + 1][x] == y[z + 3][x] == side and y[z + 2][x] == y[z][x] == 0:
                    self.three += 1
                    return '%d,%d' % ((z + 2), x)
                elif y[z + 1][x] == y[z + 2][x] == side and y[z][x] == y[z + 3][x] == 0:
                    self.three += 1
                    return '%d,%d' % (z, x)

    def dec_test(self, num, x, z, y, side):
        if num == 5:
            if 0 <= x <= 10 and 0 <= z <= 10:
                if y[z][x] == y[z + 1][x + 1] == y[z + 2][x + 2] == y[z + 3][x + 3] == side and  y[z + 4][x + 4] == 0:
                    self.five += 1
                    return '%d,%d' % ((z + 4), (x + 4))
                elif y[z][x] == y[z + 1][x + 1] == y[z + 2][x + 2] == y[z + 4][x + 4] == side and  y[z + 3][x + 3] == 0:
                    self.five += 1
                    return '%d,%d' % ((z + 3), (x + 3))
                elif y[z][x] == y[z + 1][x + 1] == y[z + 3][x + 3] == y[z + 4][x + 4] == side and  y[z + 2][x + 2] == 0:
                    self.five += 1
                    return '%d,%d' % ((z + 2), (x + 2))
                elif y[z][x] == y[z + 2][x + 2] == y[z + 3][x + 3] == y[z + 4][x + 4] == side and  y[z + 1][x + 1] == 0:
                    self.five += 1
                    return '%d,%d' % ((z + 1), (x + 1))
                elif y[z + 1][x + 1] == y[z + 2][x + 2] == y[z + 3][x + 3] == y[z + 4][x + 4] == side and  y[z][x] == 0:
                    self.five += 1
                    return '%d,%d' % (z, x)


        if num == 4:
            if 1 <= x <= 10 and 1 <= z <= 10:
                if y[z + 1][x + 1] == y[z + 2][x + 2] == y[z + 3][x + 3] == side and y[z][x] == y[z + 4][x + 4] == 0:
                    if y[z - 1][x - 1] == 0:
                        self.four += 1
                        return '%d,%d' % (z, x)
                elif y[z][x] == y[z + 1][x + 1] == y[z + 2][x + 2] == side and y[z - 1][x - 1] == y[z + 3][x + 3] == 0:
                    if y[z + 4][x + 4] == 0:
                        self.four += 1
                        return '%d,%d' % ((z + 3), (x + 3))
            if 0 <= x <= 10 and 0 <= z <= 10:
                if y[z + 1][x + 1] == y[z + 2][x + 2] == y[z + 4][x + 4] == side and y[z + 3][x + 3] == y[z][x] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 3), (x + 3))
                elif y[z + 1][x + 1] == y[z + 3][x + 3] == y[z + 4][x + 4] == side and y[z + 2][x + 2] == y[z][x] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 2), (x + 2))
                elif y[z][x] == y[z + 1][x + 1] == y[z + 3][x + 3] == side and y[z + 2][x + 2] == y[z + 4][x + 4] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 2), (x + 2))
                elif y[z][x] == y[z + 2][x + 2] == y[z + 3][x + 3] == side and y[z + 1][x + 1] == y[z + 4][x + 4] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 1), (x + 1))


        if num == 3:
            if 0 <= x <= 11 and 0 <= z <= 11:
                if y[z][x] == y[z + 1][x + 1] == y[z + 2][x + 2] == side and y[z + 3][x + 3] == 0:
                    self.three += 1
                    return '%d,%d' % ((z + 3), (x + 3))
                elif y[z + 1][x + 1] == y[z + 2][x + 2] == y[z + 3][x + 3] == side and y[z][x] == 0:
                    self.three += 1
                    return '%d,%d' % (z, x)
                elif y[z][x] == y[z + 2][x + 2] == side and y[z + 1][x + 1] == y[z + 3][x + 3] == 0:
                    self.three += 1
                    return'%d,%d' % ((z + 1), (x + 1))
                elif y[z + 1][x + 1] == y[z + 3][x + 3] == side and y[z + 2][x + 2] == y[z][x] == 0:
                    self.three += 1
                    return'%d,%d' % ((z + 2), (x + 2))
                elif y[z + 1][x + 1] == y[z + 2][x + 2] == side and y[z][x] == y[z + 3][x + 3] == 0:
                    self.three += 1
                    return'%d,%d' % (z, x)

    def inc_test(self, num, x, z, y, side):
        if num == 5:
            if 4 <= x <= 14 and 0 <= z <= 10:
                if y[z][x] == y[z + 1][x - 1] == y[z + 2][x - 2] == y[z + 3][x - 3] == side and y[z + 4][x - 4] == 0:
                    self.five += 1
                    return '%d,%d' % ((z + 4), (x - 4))
                elif y[z][x] == y[z + 1][x - 1] == y[z + 2][x - 2] == y[z + 4][x - 4] == side and y[z + 3][x - 3] == 0:
                    self.five += 1
                    return '%d,%d' % ((z + 3), (x - 3))
                elif y[z][x] == y[z + 1][x - 1] == y[z + 3][x - 3] == y[z + 4][x - 4] == side and y[z + 2][x - 2] == 0:
                    self.five += 1
                    return '%d,%d' % ((z + 2), (x - 2))
                elif y[z][x] == y[z + 2][x - 2] == y[z + 3][x - 3] == y[z + 4][x - 4] == side and y[z + 1][x - 1] == 0:
                    self.five += 1
                    return '%d,%d' % ((z + 1), (x - 1))
                elif y[z + 1][x - 1] == y[z + 2][x - 2] == y[z + 3][x - 3] == y[z + 4][x - 4] == side and y[z][x] == 0:
                    self.five += 1
                    return '%d,%d' % (z, x)

        if num == 4:
            if 5 <= x <= 14 and 0 <= z <= 9:
                if y[z + 2][x - 2] == y[z + 3][x - 3] == y[z + 4][x - 4] == side and y[z + 1][x - 1] == y[z + 5][x - 5] == 0:
                    if y[z][x] == 0:
                        self.four += 1
                        return '%d,%d' % ((z + 1), (x - 1))
                if y[z + 1][x - 1] == y[z + 2][x - 2] == y[z + 3][x - 3] == side and y[z][x] == y[z + 4][x - 4] == 0:
                    if y[z + 5][x - 5] == 0:
                        self.four += 1
                        return '%d,%d' % ((z + 4), (x - 4))
            if 4 <= x <= 14 and 0 <= z <= 10:
                if y[z + 1][x - 1] == y[z + 2][x - 2] == y[z + 4][x - 4] == side and y[z + 3][x - 3] == y[z][x] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 3), (x - 3))
                elif y[z + 1][x - 1] == y[z + 3][x - 3] == y[z + 4][x - 4] == side and y[z + 2][x - 2] == y[z][x] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 2), (x - 2))
                elif y[z][x] == y[z + 1][x - 1] == y[z + 3][x - 3] == side and y[z + 2][x - 2] == y[z + 4][x - 4] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 2), (x - 2))
                elif y[z][x] == y[z + 2][x - 2] == y[z + 3][x - 3] == side and y[z + 1][x - 1] == y[z + 4][x - 4] == 0:
                    self.four += 1
                    return '%d,%d' % ((z + 1), (x - 1))


        if num == 3:
            if 3 <= x <= 14 and 0 <= z <= 11:
                if y[z][x] == y[z + 1][x - 1] == y[z + 2][x - 2] == side and y[z + 3][x - 3] == 0:
                    self.three += 1
                    return '%d,%d' % ((z + 3), (x - 3))
                elif y[z + 1][x - 1] == y[z + 2][x - 2] == y[z + 3][x - 3] == side and y[z][x] == 0:
                    self.three += 1
                    return '%d,%d' % (z, x)
                elif y[z][x] == y[z + 2][x - 2] == side and y[z + 1][x - 1] == y[z + 4][x - 4] == 0:
                    self.three += 1
                    return '%d,%d' % ((z + 1), (x - 1))
                elif y[z + 1][x - 1] == y[z + 3][x - 3] == side and y[z + 2][x - 2] == y[z][x] == 0:
                    self.three += 1
                    return '%d,%d' % ((z + 2), (x - 2))
                elif y[z + 1][x - 1] == y[z + 2][x - 2] == side and y[z][x] == y[z + 3][z - 3] == 0:
                    self.three += 1
                    return '%d,%d' % (z, x)

    def special(self, num, x, z, y, side):
        pass

    def judge(self, y, side):
        self.five = 0
        self.four = 0
        self.three = 0
        self.result = []
        result = self.result
        for x in range(15):
            for z in range(15):
                result.append(self.row_test(5, x, z, y, side))
                result.append(self.col_test(5, x, z, y, side))
                result.append(self.dec_test(5, x, z, y, side))
                result.append(self.inc_test(5, x, z, y, side))
        while None in result:
            result.remove(None)
        if len(result) == 0:
            for x in range(15):
                for z in range(15):
                    result.append(self.row_test(4, x, z, y, side))
                    result.append(self.col_test(4, x, z, y, side))
                    result.append(self.dec_test(4, x, z, y, side))
                    result.append(self.inc_test(4, x, z, y, side))
        while None in result:
            result.remove(None)
        if len(result) == 0:
            for x in range(15):
                for z in range(15):
                    result.append(self.row_test(3, x, z, y, side))
                    result.append(self.col_test(3, x, z, y, side))
                    result.append(self.dec_test(3, x, z, y, side))
                    result.append(self.inc_test(3, x, z, y, side))

        while None in result:
            result.remove(None)

    def AIC(self, y):
        ch1 = []
        ch2 = []
        self.judge(y, 1)
        result = self.result
        five1 =self.five
        four1 = self.four
        three1 = self.three
        for each in result:
            ch1.append(each.split(','))
        if len(ch1) >= 1:
            i = r.randint(0, (len(ch1)-1))
            v = int(ch1[i][0])
            h = int(ch1[i][1])
        else:
            i = r.randint(5, 9)
            k = r.randint(5, 9)
            while y [i][k] != 0:
                i = r.randint(5, 9)
                k = r.randint(5, 9)
            v = i
            h = k

        self.judge(y, -1)
        result = self.result
        five2 =self.five
        four2 = self.four
        three2 = self.three
        for each in result:
            ch2.append(each.split(','))
        if len(ch2) >= 1:
            i = r.randint(0, (len(ch2) - 1))
            m = int(ch2[i][0])
            n = int(ch2[i][1])
        else:
            i = r.randint(5, 9)
            k = r.randint(5, 9)
            while y[i][k] != 0:
                i = r.randint(5, 9)
                k = r.randint(5, 9)
            m = i
            n = k

        if five1 > 0 and five2 > 0:
            y[m][n] = -1
        elif five1 == 0 and five2 > 0:
            y[m][n] = -1
        elif five1 > 0 and five2 == 0:
            y[v][h] = -1
        elif five1 == five2 == 0 and four1 > 0 and four2 > 0:
            y[m][n] = -1
        elif five1 == five2 == 0 and four1 == 0 and four2 > 0:
            y[m][n] = -1
        elif five1 == five2 == 0 and four1 > 0 and four2 == 0:
            y[v][h] = -1
        elif five1 == five2 == four1 == four2 == 0 and three1 > 0 and three2 > 0:
            y[m][n] = -1
        elif five1 == five2 == four1 == four2 == 0 and three1 == 0 and three2 > 0:
            y[m][n] = -1
        elif five1 == five2 == four1 == four2 == 0 and three1 > 0 and three2 == 0:
            y[v][h] = -1
        elif five1 == five2 == four1 == four2 == three1 == three2 == 0:
            y[v][h] = -1

