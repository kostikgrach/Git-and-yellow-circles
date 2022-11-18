from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5 import uic
import sys
import random

SCREEN_SIZE = [400, 400]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.coords = []
        self.btn.clicked.connect(self.draw)


    def draw(self):
        self.size = random.randint(10, 100)
        self.color = QColor('#FFFF00')
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(self.color))
            qp.setBrush(QColor(self.color))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
