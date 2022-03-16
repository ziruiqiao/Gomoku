from PyQt5.QtCore import Qt, QPoint, QTimer
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPixmap, QRadialGradient, QPalette
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import traceback
from Gomokugame import Gomoku

def run_with_exc(f):
    def call(window, *args, **kwargs):
        try:
            return f(window, *args, **kwargs)
        except Exception:
            exc_info = traceback.format_exc()
            QMessageBox.about(window, 'ERROR MESSAGE', exc_info)
    return call

class GomokuWindow (QMainWindow):

    def __init__(self):
        super().__init__()
        self.g = Gomoku()  #initial game content
        self.init_ui()  #initial game window
        self.res = 0

    def init_ui(self):

        # 1. define game window title, size and color
        self.setObjectName('MainWindow')
        self.setWindowTitle('Gomoku')
        self.setFixedSize(650, 650)
        self.setStyleSheet('#MainWindow{background-color: silver}') #cyan
        # 2. initial game content
        self.show()

    def paintEvent(self, e):
        # draw game content
        
        def draw_map():
            # draw board
            qp.setPen(QPen (QColor (0, 0, 0), 2, Qt.SolidLine))  #board color is black

            # draw horizontal lines
            for x in range(15):
                qp.drawLine(40 * (x + 1), 40, 40 * (x + 1), 600)

            #draw vertical lines
            for y in range(15):
                qp.drawLine(40, 40 * (y + 1), 600, 40 * (y + 1))

            qp.setPen(QPen (QColor(0, 0, 0), 1, Qt.SolidLine))
            qp.setBrush(QColor(0, 0, 0))
            qp.drawEllipse(QPoint(40 * (8), 40 * (8)), 5, 5)
            qp.drawEllipse(QPoint(40 * (3 + 1), 40 * (3 + 1)), 5, 5)
            qp.drawEllipse(QPoint(40 * (3 + 1), 40 * (8)), 5, 5)
            qp.drawEllipse(QPoint(40 * (3 + 1), 40 * (12)), 5, 5)
            qp.drawEllipse(QPoint(40 * (8), 40 * (3 + 1)), 5, 5)
            qp.drawEllipse(QPoint(40 * (8), 40 * (12)), 5, 5)
            qp.drawEllipse(QPoint(40 * (12), 40 * (3 + 1)), 5, 5)
            qp.drawEllipse(QPoint(40 * (12), 40 * (8)), 5, 5)
            qp.drawEllipse(QPoint(40 * (12), 40 * (12)), 5, 5)
            
        def draw_pieces(self):
            # draw black pieces
            qp.setPen(QPen (QColor(0, 0, 0), 1, Qt.SolidLine))
            qp.setBrush(QColor(0, 0, 0))
            for x in range(15):
                for z in range(15):
                    if self.g.y[z][x] == 1:
                        qp.drawEllipse(QPoint(40 * (x + 1), 40 * (z + 1)), 15, 15)

            # draw white pieces
            qp.setPen(QPen (QColor(255, 255, 255), 1, Qt.SolidLine))
            qp.setBrush(QColor(255, 255, 255))
            for x in range(15):
                for z in range(15):
                    if self.g.y[z][x] == -1:
                        qp.drawEllipse(QPoint(40 * (x + 1), 40 * (z + 1)), 15, 15)

        self.t = 0
        qp = QPainter()
        qp.begin(self)
        draw_map()
        draw_pieces(self)
        qp.end()
        
            
    @run_with_exc
    def mousePressEvent(self, e):
        
        # mouse clicking put pieces
        mouse_x = e.windowPos().x()
        mouse_y = e.windowPos().y()
        if (mouse_x % 40 <= 15 or mouse_x % 40 >= 25) and (mouse_y % 40 <= 15 or mouse_y % 40 >= 25):
            game_x = int((mouse_x + 15) // 40) - 1
            game_y = int((mouse_y + 15) // 40) - 1
        else:
            return
        self.g.move_1step(True, game_x, game_y)
            
        self.g.game_result(1)
        res = self.g.S
        if res != 0:
            self.repaint(0, 0, 650, 650)
                #self.show(res)
            self.game_restart(res)
            return
        self.g.ai_move_1step()
        self.g.game_result(-1)
        res = self.g.S
        if res != 0:
            self.repaint(0, 0, 650, 650)
                #self.show(res)
            self.game_restart(res)
            return
        self.repaint(0, 0, 650, 650)

    def game_restart(self, res):
        self.res = res
        if self.res == 1:
            QMessageBox.about(self, 'Game Over', 'You Win!!')
        elif self.res == -1:
            QMessageBox.about(self, 'Game Over', 'You Lose')
        elif self.res == 2:
            QMessageBox.about(self, 'Game Over', 'Draw Game!')
