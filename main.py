import sys, csv, os

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QComboBox, QLabel, QPushButton, \
    QLineEdit
from PyQt5.QtGui import QIcon


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lbl = None
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        data = open('Final_Data.csv', 'r')
        reader = csv.reader(data)
        reader = list(reader)

        qle = QLineEdit(self)
        qle.setGeometry(QRect(50, 200, 500, 60))
        btn = QPushButton('Run', self)
        btn.setGeometry(QRect(550, 200, 200, 60))
        btn.clicked.connect(lambda: self.pm3(reader[int(qle.text())][2], reader[int(qle.text())][3]))
        search = QPushButton('Search', self)
        search.setGeometry(QRect(50, 300, 200, 60))
        self.setGeometry(300, 300, 800, 480)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('GUI')
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onActivated(self, text):
        self.statusBar().showMessage(text + ' was selected')

    def pm3(self, text, text2):
        os.system('proxmark3 -p /dev/ttyACM0 -c "' + text + '"')
        os.system('proxmark3 -p /dev/ttyACM0 -c "' + text2 + '"')

    # def search(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
