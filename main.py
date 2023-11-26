from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random


class Git_Yellow_Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor('yellow'))
            qp.setBrush(QColor('yellow'))
            self.x, self.y = random.randint(0, 400), random.randint(0, 400)
            self.size = random.randint(10, 200)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Git_Yellow_Circles()
    ex.show()
    sys.exit(app.exec())