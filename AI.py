import random as r

class AI:

    def __init__(self):
        self.result = []
        self.four = 0
        self.three = 0

    def judge(self,side,y):

        two = 0
        three = self.three
        four = self.four
        three = 0
        four = 0
        common1 = ['4row','4col','4decline','4incline','3row','3col','3decline','3incline','2row','2col','2decline','2incline']
        spe3 = ['4special3R-','4special3R+','4special3C-','4special3C+','4special3D-','4special3D+''4special3I-''4special3I+']
        spe2_4 = ['4special2R-','4special2R+','4special2C-','4special2C+','4special2D-','4special2D+''4special2I-''4special2I+']
        spe2_3 = ['3special2R-','3special2R+','3special2C-','3special2C+','3special2D-','3special2D+''3special2I-''3special2I+']
        realspe2_4 = ['4speIL','4speIR','4speDL','4speDR','4speRL','4speRR','4speCL','4speCR']
        allkind = common1 + spe3 + spe2_4 + spe2_3 + realspe2_4
        kind = []
        location = []
        result = self.result
        dic = {}

        #judge situation
        for eachrow in range(15):
            for eachcol in range(15):

    # 4---------------------------------------------------------------------------------------------------------------------------------

                contirow1 = 1
                conticol1 = 1
                contidecline1 = 1
                contiincline1 = 1
                # Oooo
                try:
                    if y[eachrow][eachcol] == y[eachrow][eachcol + 1] == y[eachrow][eachcol + 2] == y[eachrow][eachcol + 3] == side:
                        contirow1 -= 1
                        try:
                            if y[eachrow][eachcol + 4] == 0:
                                kind.append('4row')
                                location.append('%d,%d'% (eachrow, (eachcol + 4)))
                            elif y[eachrow][eachcol - 1] == 0:
                                kind.append('4row')
                                location.append('%d,%d'% (eachrow, (eachcol - 1)))
                        except IndexError:
                            if y[eachrow][eachcol - 1] == 0:
                                kind.append('4row')
                                location.append('%d,%d'% (eachrow, (eachcol - 1)))
                            elif y[eachrow][eachcol + 4] == 0:
                                kind.append('4row')
                                location.append('%d,%d'% (eachrow, (eachcol + 4)))
                except IndexError:
                    pass

                # O
                # o
                # o
                # o
                try:
                    if y[eachrow][eachcol] == y[eachrow + 1][eachcol] == y[eachrow + 2][eachcol] == y[eachrow + 3][eachcol] == side:
                        conticol1 -= 1
                        try:
                            if y[eachrow + 4][eachcol] == 0:
                                kind.append('4col')
                                location.append('%d,%d'% ((eachrow + 4),eachcol))
                            elif y[eachrow - 1][eachcol] == 0:
                                kind.append('4col')
                                location.append('%d,%d'% ((eachrow - 1),eachcol))
                        except IndexError:
                            if y[eachrow - 1][eachcol] == 0:
                                kind.append('4col')
                                location.append('%d,%d'% ((eachrow - 1),eachcol))
                            elif y[eachrow + 4][eachcol] == 0:
                                kind.append('4col')
                                location.append('%d,%d'% ((eachrow + 4),eachcol))
                except IndexError:
                    pass

                # O
                #   o
                #     o
                #       o
                try:
                    if y[eachrow][eachcol] == y[eachrow + 1][eachcol + 1] == y[eachrow + 2][eachcol + 2] == y[eachrow + 3][eachcol + 3] == side:
                        contidecline1 -= 1
                        try:
                            if y[eachrow + 4][eachcol + 4] == 0:
                                kind.append('4decline')
                                location.append('%d,%d'% ((eachrow + 4),(eachcol + 4)))
                            elif y[eachrow - 1][eachcol - 1] == 0:
                                kind.append('4decline')
                                location.append('%d,%d'% ((eachrow - 1),(eachcol - 1)))
                        except IndexError:
                            try:
                                if y[eachrow + 4][eachcol + 4] == 0:
                                    kind.append('4decline')
                                    location.append('%d,%d'% ((eachrow + 4),(eachcol + 4)))
                            except IndexError:
                                if y[eachrow - 1][eachcol - 1] == 0:
                                    kind.append('4decline')
                                    location.append('%d,%d'% ((eachrow - 1),(eachcol - 1)))
                except IndexError:
                    pass

                #       O
                #     o
                #   o
                # o
                try:
                    if y[eachrow][eachcol] == y[eachrow + 1][eachcol - 1] == y[eachrow + 2][eachcol - 2] == y[eachrow + 3][eachcol - 3] == side:
                        contiincline1 -= 1
                        try:
                            if y[eachrow + 4][eachcol - 4] == 0:
                                kind.append('4incline')
                                location.append('%d,%d'% ((eachrow + 4),(eachcol - 4)))
                            elif y[eachrow - 1][eachcol + 1] == 0:
                                kind.append('4incline')
                                location.append('%d,%d'% ((eachrow - 1),(eachcol + 1)))

                        except IndexError:
                            try:
                                if y[eachrow + 4][eachcol - 4] == 0:
                                    kind.append('4incline')
                                    location.append('%d,%d'% ((eachrow + 4),(eachcol - 4)))
                            except IndexError:
                                if y[eachrow - 1][eachcol + 1] == 0:
                                    kind.append('4incline')
                                    location.append('%d,%d'% ((eachrow - 1),(eachcol + 1)))
                except IndexError:
                    pass

    # 3---------------------------------------------------------------------------------------------------------------------------------
                contirow3 = 1
                conticol3 = 1
                contidecline3 = 1
                contiincline3 = 1

                # Ooo
                try:
                    if contirow1 and y[eachrow][eachcol] == y[eachrow][eachcol + 1] == y[eachrow][eachcol + 2] == side:
                        contirow3 -= 1
                        conti2 = 1
                        # o Ooo
                        try:
                            if conti2 and y[eachrow][eachcol - 2] == side and y[eachrow][eachcol - 1] == 0:
                                kind.append('4special3R-')
                                location.append('%d,%d'% (eachrow,(eachcol - 1)))
                                conti2 -= 1
                        except IndexError:
                            pass
                        # Ooo o
                        try:
                            if conti2 and y[eachrow][eachcol + 4] == side and y[eachrow][eachcol + 3] == 0:
                                kind.append('4special3R+')
                                location.append('%d,%d' % (eachrow, (eachcol + 3)))
                                conti2 -= 1
                        except IndexError:
                            pass
                        # Ooo
                        try:
                            if conti2 and y[eachrow][eachcol - 1] == 0 and y[eachrow][eachcol + 3] == 0 and not y[eachrow][eachcol - 2] == y[eachrow][eachcol + 4] == -side:
                                kind.append('3row')
                                location.append('%d,%d;%d,%d'% (eachrow,(eachcol - 1),eachrow,(eachcol + 3)))
                                conti2 -= 1
                        except IndexError:
                            pass
                except IndexError:
                    pass

                # O
                # o
                # o
                try:
                    if conticol1 and y[eachrow][eachcol] == y[eachrow + 1][eachcol] == y[eachrow + 2][eachcol] == side:
                        conticol3 -= 1
                        conti2 = 1
                        # o
                        #
                        # O
                        # o
                        # o
                        try:
                            if conti2 and y[eachrow - 2][eachcol] == side and y[eachrow - 1][eachcol] == 0:
                                kind.append('4special3C-')
                                location.append('%d,%d'% ((eachrow - 1),eachcol))
                                conti2 -= 1
                        except IndexError:
                            pass
                        # O
                        # o
                        # o
                        #
                        # o
                        try:
                            if conti2 and y[eachrow + 4][eachcol] == side and y[eachrow + 3][eachcol] == 0:
                                kind.append('4special3C+')
                                location.append('%d,%d' % ((eachrow + 3), eachcol))
                                conti2 -= 1
                        except IndexError:
                            pass
                        # O
                        # o
                        # o
                        try:
                            if conti2 and y[eachrow - 1][eachcol] == 0 and y[eachrow + 3][eachcol] == 0 and not y[eachrow - 2][eachcol] == y[eachrow + 4][eachcol] == -side:
                                kind.append('3col')
                                location.append('%d,%d;%d,%d'% ((eachrow - 1),eachcol,(eachrow + 3),eachcol))
                                conti2 -= 1
                        except IndexError:
                            pass
                except IndexError:
                    pass

                # O
                #   o
                #     o
                try:
                    if contidecline1 and y[eachrow][eachcol] == y[eachrow + 1][eachcol + 1] == y[eachrow + 2][eachcol + 2] == side:
                        contidecline3 -= 1
                        conti2 = 1
                        # o
                        #
                        #     O
                        #       o
                        #         o
                        try:
                            if conti2 and y[eachrow - 2][eachcol - 2] == side and y[eachrow - 1][eachcol - 1] == 0:
                                kind.append('4special3D-')
                                location.append('%d,%d'% ((eachrow - 1),(eachcol - 1)))
                                conti2 -= 1
                        except IndexError:
                            pass
                        # O
                        #   o
                        #     o
                        #
                        #         o
                        try:
                            if conti2 and y[eachrow + 4][eachcol + 4] == side and y[eachrow + 3][eachcol + 3] == 0:
                                kind.append('4special3D+')
                                location.append('%d,%d' % ((eachrow + 3), (eachcol + 3)))
                                conti2 -= 1
                        except IndexError:
                            pass
                        #     O
                        #       o
                        #         o
                        try:
                            if conti2 and y[eachrow - 1][eachcol - 1] == 0 and y[eachrow + 3][eachcol + 3] == 0 and not y[eachrow - 2][eachcol - 2] == y[eachrow + 4][eachcol + 4] == -side:
                                kind.append('3decline')
                                location.append('%d,%d;%d,%d'% ((eachrow - 1),(eachcol - 1),(eachrow + 3),(eachcol + 3)))
                                conti2 -= 1
                        except IndexError:
                            pass
                except IndexError:
                    pass

                #     O
                #   o
                # o
                try:
                    if contiincline1 and y[eachrow][eachcol] == y[eachrow + 1][eachcol - 1] == y[eachrow + 2][eachcol - 2] == side:
                        contiincline3 -= 1
                        conti2 = 1
                        #         o
                        #
                        #     O
                        #   o
                        # o
                        try:
                            if conti2 and y[eachrow - 2][eachcol + 2] == side and y[eachrow - 1][eachcol + 1] == 0:
                                kind.append('4special3I-')
                                location.append('%d,%d'% ((eachrow - 1),(eachcol + 1)))
                                conti2 -= 1
                        except IndexError:
                            pass
                        #         O
                        #       o
                        #     o
                        #
                        # o
                        try:
                            if conti2 and y[eachrow + 4][eachcol - 4] == side and y[eachrow + 3][eachcol - 3] == 0:
                                kind.append('4special3I+')
                                location.append('%d,%d' % ((eachrow + 3), (eachcol - 3)))
                                conti2 -= 1
                        except IndexError:
                             pass
                        #     O
                        #   o
                        # o
                        try:
                            if conti2 and y[eachrow - 1][eachcol + 1] == 0 and y[eachrow + 3][eachcol - 3] == 0 and not y[eachrow - 2][eachcol + 2] == y[eachrow + 4][eachcol - 4] == -side:
                                kind.append('3incline')
                                location.append('%d,%d;%d,%d'% ((eachrow - 1),(eachcol + 1),(eachrow + 3),(eachcol - 3)))
                                conti2 -= 1
                        except IndexError:
                            pass
                except IndexError:
                    pass


    # 2----------------------------------------------------------------------------------------------------------------------------------
                # Oo
                try:
                    if contirow1 and contirow3 and y[eachrow][eachcol] == y[eachrow][eachcol + 1] == side:
                        conti4 = 1
                        # o Oo
                        try:
                            if conti4 and y[eachrow][eachcol - 2] == side:
                                conti5 = 1
                                conti4 -= 1
                                # oo Oo
                                try:
                                    if conti5 and y[eachrow][eachcol - 3] == side and y[eachrow][eachcol - 1] == 0:
                                        kind.append('4special2R-')
                                        location.append('%d,%d' % (eachrow, (eachcol - 1)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                # o Oo
                                try:
                                    if conti5 and (y[eachrow][eachcol - 3] == 0 or  y[eachrow][eachcol + 2] == 0) and y[eachrow][eachcol - 1] == 0:
                                        kind.append('3special2R-')
                                        location.append('%d,%d;-1,-1'% (eachrow,(eachcol - 1)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    pass
                        except IndexError:
                            pass
                        # Oo o
                        try:
                            if conti4 and y[eachrow][eachcol + 3] == side:
                                conti5 = 1
                                conti4 -= 1
                                # Oo oo
                                try:
                                    if conti5 and y[eachrow][eachcol + 4] == side and y[eachrow][eachcol + 2] == 0:
                                        kind.append('4special2R+')
                                        location.append('%d,%d' % (eachrow, (eachcol + 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                # Oo o
                                try:
                                    if conti5 and (y[eachrow][eachcol + 4] == 0 or y[eachrow][eachcol - 1] == 0) and y[eachrow][eachcol + 2] == 0:
                                        kind.append('3special2R+')
                                        location.append('%d,%d;-1,-1' % (eachrow, (eachcol + 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    pass
                        except IndexError:
                            pass
                        # Oo
                        try:
                            if conti4 and y[eachrow][eachcol - 1] == 0 and y[eachrow][eachcol + 2] == 0:
                                conti5 = 1
                                conti4 -= 1
                                # o
                                #  Oo
                                # o
                                try:
                                    if conti5 and y[eachrow + 1][eachcol - 1] == y[eachrow -1][eachcol - 1] == side and y[eachrow + 2][eachcol - 1] == 0 and y[eachrow -2][eachcol - 1] == 0 and y[eachrow][eachcol - 1] == 0:
                                        kind.append('4speRL')
                                        location.append('%d,%d' % (eachrow, (eachcol - 1)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                #   o
                                # Oo
                                #   o
                                try:
                                    if conti5 and y[eachrow + 1][eachcol + 2] == y[eachrow -1][eachcol + 2] ==side and y[eachrow + 2][eachcol + 2] == 0 and y[eachrow -2][eachcol + 2] == 0 and y[eachrow][eachcol + 2] == 0:
                                        kind.append('4speRR')
                                        location.append('%d,%d' % (eachrow, (eachcol + 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                # oo
                                if conti5 and y[eachrow][eachcol - 1] == 0 and y[eachrow][eachcol + 2] == 0:
                                    kind.append('2row')
                                    location.append('%d,%d;%d,%d'% (eachrow,(eachcol - 1),eachrow,(eachcol + 2)))
                        except IndexError:
                            pass
                except IndexError:
                    pass

                # O
                # o
                try:
                    if conticol1 and conticol3 and y[eachrow][eachcol] == y[eachrow + 1][eachcol] == side:
                        conti4 = 1
                        # o
                        #
                        # O
                        # o
                        try:
                            if conti4 and y[eachrow - 2][eachcol] == side:
                                conti5 = 1
                                conti4 -= 1
                                # o
                                # o
                                #
                                # O
                                # o
                                try:
                                    if conti5 and y[eachrow - 3][eachcol] == side:
                                        kind.append('4special2C-')
                                        location.append('%d,%d' % ((eachrow - 1), eachcol))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                try:
                                    if conti5 and y[eachrow - 3][eachcol] == 0 or y[eachrow + 2][eachcol] == 0:
                                        kind.append('3special2C-')
                                        location.append('%d,%d;-1,-1' % ((eachrow - 1), eachcol))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    pass
                        except IndexError:
                            pass
                        # O
                        # o
                        #
                        # o
                        try:
                            if conti4 and y[eachrow + 3][eachcol] == side:
                                conti5 = 1
                                conti4 -= 1
                                try:
                                    if conti5 and y[eachrow + 4][eachcol] == side:
                                        kind.append('4special2C+')
                                        location.append('%d,%d' % ((eachrow + 2), eachcol))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                try:
                                    if conti5 and y[eachrow + 4][eachcol] == 0 or y[eachrow - 1][eachcol] == 0:
                                        kind.append('3special2C+')
                                        location.append('%d,%d;-1,-1' % ((eachrow + 2), eachcol))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    pass
                        except IndexError:
                            pass

                        # O
                        # o
                        try:
                            if conti4 and y[eachrow - 1][eachcol] != -side and y[eachrow + 2][eachcol] != -side:
                                conti5 = 1
                                conti4 -= 1
                                try:
                                    if conti5 and y[eachrow - 1][eachcol - 1] == y[eachrow -1][eachcol + 1] ==side and y[eachrow - 1][eachcol - 2] != -side and y[eachrow - 1][eachcol + 2] != -side:
                                        kind.append('4speCD')
                                        location.append('%d,%d' % ((eachrow - 1), eachcol))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                try:
                                    if conti5 and y[eachrow + 2][eachcol - 1] == y[eachrow + 2][eachcol + 1] ==side and y[eachrow + 2][eachcol + 2] != -side and y[eachrow + 2][eachcol - 2] != -side:
                                        kind.append('4speCU')
                                        location.append('%d,%d' % (eachrow, (eachcol + 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    kind.append('2col')
                                    location.append('%d,%d;%d,%d'% ((eachrow - 1),eachcol,(eachrow + 2),eachcol))
                        except IndexError:
                            pass
                except IndexError:
                    pass

                # O
                #   o
                try:
                    if contidecline1 and contidecline3 and y[eachrow][eachcol] == y[eachrow + 1][eachcol + 1] == side:
                        conti4 = 1
                        try:
                            if conti4 and y[eachrow - 2][eachcol - 2] == side:
                                conti5 = 1
                                conti4 -= 1
                                try:
                                    if conti5 and y[eachrow - 3][eachcol - 3] == side:
                                        kind.append('4special2D-')
                                        location.append('%d,%d' % ((eachrow - 1), (eachcol - 1)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                try:
                                    if conti5 and y[eachrow - 3][eachcol - 3] == 0 or y[eachrow + 2][eachcol + 2] == 0:
                                        kind.append('3special2D-')
                                        location.append('%d,%d;-1,-1' % ((eachrow - 1), (eachcol - 1)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    pass
                        except IndexError:
                            pass
                        try:
                            if conti4 and y[eachrow + 3][eachcol + 3] == side:
                                conti5 = 1
                                conti4 -= 1
                                try:
                                    if y[eachrow + 4][eachcol + 4] == side:
                                        kind.append('4special2D+')
                                        location.append('%d,%d' % ((eachrow + 2), (eachcol + 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                try:
                                    if y[eachrow + 4][eachcol + 4] == 0 or y[eachrow - 1][eachcol - 1] == 0:
                                        kind.append('3special2D+')
                                        location.append('%d,%d,-1,-1' % ((eachrow + 2), (eachcol + 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    pass
                        except IndexError:
                            pass
                        try:
                            if conti4 and y[eachrow - 1][eachcol - 1] != -side and y[eachrow + 2][eachcol + 2] != -side:
                                conti5 = 1
                                conti4 -= 1
                                try:
                                    if conti5 and y[eachrow][eachcol - 2] == y[eachrow -2][eachcol] ==side and y[eachrow + 2][eachcol - 3] != -side and y[eachrow - 3][eachcol + 2] != -side:
                                        kind.append('4speDL')
                                        location.append('%d,%d' % ((eachrow - 1), (eachcol - 1)))
                                        conti5 = False
                                except IndexError:
                                    pass
                                try:
                                    if conti5 and y[eachrow + 3][eachcol + 1] == y[eachrow + 1][eachcol + 3] ==side and y[eachrow + 4][eachcol] != -side and y[eachrow][eachcol + 4] != -side:
                                        kind.append('4speDR')
                                        location.append('%d,%d' % ((eachrow + 2), (eachcol + 2)))
                                        conti5 -= 1
                                except IndexError:
                                        pass
                                if conti5:
                                    kind.append('2decline')
                                    location.append('%d,%d;%d,%d'% ((eachrow - 1),(eachcol - 1),(eachrow + 2),(eachcol + 2)))
                        except IndexError:
                            pass
                except IndexError:
                    pass

                #   O
                # o
                try:
                    if contiincline1 and contiincline3 and y[eachrow][eachcol] == y[eachrow + 1][eachcol - 1] == side:
                        conti4 = 1
                        try:
                            if conti4 and y[eachrow - 2][eachcol + 2] == side:
                                conti5 = 1
                                conti4 -= 1
                                try:
                                    if conti5 and y[eachrow - 3][eachcol + 3] == side:
                                        kind.append('4special2I-')
                                        location.append('%d,%d' % ((eachrow - 1), (eachcol + 1)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                try:
                                    if y[eachrow - 3][eachcol + 3] == 0 or y[eachrow + 2][eachcol - 2] == 0:
                                        kind.append('3special2I-')
                                        location.append('%d,%d;-1,-1' % ((eachrow - 1), (eachcol + 1)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    pass
                        except IndexError:
                            pass
                        try:
                            if conti4 and y[eachrow + 3][eachcol - 3] == side:
                                conti4 -= 1
                                conti5 = 1
                                try:
                                    if conti5 and y[eachrow + 4][eachcol - 4] == side:
                                        kind.append('4special2I+')
                                        location.append('%d,%d' % ((eachrow + 2), (eachcol - 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                try:
                                    if y[eachrow + 4][eachcol - 4] == 0 or y[eachrow - 1][eachcol + 1] == 0:
                                        kind.append('3special2I+')
                                        location.append('%d,%d;-1,-1' % ((eachrow + 2), (eachcol - 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    pass
                        except IndexError:
                            pass
                        try:
                            if y[eachrow - 1][eachcol + 1] != -side and y[eachrow + 2][eachcol - 2] != -side:
                                conti4 -= 1
                                conti5 = 1
                                try:
                                    if conti5 and y[eachrow + 3][eachcol - 1] == y[eachrow + 1][eachcol - 3] == side and y[eachrow + 4][eachcol] != -side and y[eachrow][eachcol - 4] != -side:
                                        kind.append('4speIL')
                                        location.append('%d,%d' % ((eachrow + 2), (eachcol - 2)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                try:
                                    if conti5 and y[eachrow - 2][eachcol] == y[eachrow][eachcol + 2] == side and y[eachrow - 3][eachcol - 1] != -side and y[eachrow + 1][eachcol + 3] != -side:
                                        kind.append('4speIR')
                                        location.append('%d,%d' % ((eachrow - 1), (eachcol + 1)))
                                        conti5 -= 1
                                except IndexError:
                                    pass
                                if conti5:
                                    kind.append('2incline')
                                    location.append('%d,%d;%d,%d'% ((eachrow - 1),(eachcol + 1),(eachrow + 2),(eachcol - 2)))
                                    conti5 -= 1
                        except IndexError:
                            pass
                except IndexError:
                    pass


    # --------------------------------------------------------------------------------------------------------------------------------

        # record appeared cases and its location in dic{}
        for each in range(len(kind)):
            dic[kind[each]] = location[each]

        # put cases appeared in the dictionary
        def arrange (num):
            for each in kind:
                if each[0] == num:
                    result.append(dic[each])

        # count situation appeared
        for i in kind:
            if i[0] == '4':
                four += 1
            elif i[0] == '3':
                three += 1
            elif i[0] == '2':
                two += 1

        # output possible locations
        if four >= 1 :
            arrange('4')
        elif four == 0 and three >= 0:
            arrange('3')
        elif four == 0 and three == 0:
            arrange('2')

        # make sure the possible locations are in right form
        kind.clear()
        for each in result:
            kind += each.split(';')
        result.clear()
        result += kind.copy()

                            
    def AIC(self,y):
        # simple AI player
        player = 1
        AI = -1
        Choices = []
        Choices1 = []
        temp = []
        temp1 = []
        F1 = 0
        F2 = 0
        T1 = 0
        T2 = 0
        x = []
        z = []

        # check player's condition
        self.judge(player,y)
        temp += self.result.copy()
        length1 = len(temp)
        F1 += self.four
        T1 += self.three

        # check AI's condition
        self.judge(AI,y)
        temp1 += self.result.copy()
        length2 = len(temp1)
        F2 += self.four
        T2 += self.three

        for each in temp:
            Choices.append(each.split(','))
        for each in temp1:
            Choices1.append(each.split(','))

        # put possible coord in arrays
        if (length2 + length1) == 0:
            temp1 = r.randint(6, 8)
            temp2 = r.randint(6, 8)
            while y[temp1][temp2] != 0:
                temp1 = r.randint(5, 9)
                temp2 = r.randint(5, 9)
            z.append(temp1)
            x.append(temp2)

        elif F2 >= 1:
            z.append(Choices1[0][0])
            x.append(Choices1[0][1])

        elif F1 >= 0 and F2 == 0:
            z.append(Choices[0][0])
            x.append(Choices[0][1])
                
        elif T2 >= 0:
            for i in range(length2):
                z.append(Choices1[i][0])
                x.append(Choices1[i][1])

        elif T2 == 0 and T1 >= 0:
            for i in range(length1):
                z.append(Choices[i][0])
                x.append(Choices[i][1])

        elif length2 != 0 and T2 == T1 == 0:
            for i in range(length1):
                z.append(Choices[i][0])
                x.append(Choices[i][1])
            for i in range(length2):
                z.append(Choices1[i][0])
                x.append(Choices1[i][1])

        te = len(z) - 1
        index = r.randint(0, te)
        h = int(x[index])
        v = int(z[index])

        while y[int(z[index])][int(x[index])] != 0 or v == -1 :
            index = r.randint(0, te)
            
        y[v][h] = -1
        

