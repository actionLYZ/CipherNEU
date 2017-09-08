
'''--------------------------------加载进度条------------------------------------------------------
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MessageBox(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('message box')


    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QtWidgets.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())
'''

'''--------------------------------加载进度条------------------------------------------------------

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Example(QtWidgets.QWidget):


    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.button = QtWidgets.QPushButton('Start', self)
        self.button.setFocusPolicy(QtCore.Qt
                                   .NoFocus)
        self.button.move(40, 80)

        self.button.clicked.connect(self.doAction)

        self.timer = QtCore.QBasicTimer()
        self.step = 0

        self.setWindowTitle('ProgressBar')
        self.setGeometry(300, 300, 250, 150)


    def timerEvent(self, event):

        if self.step >= 100:
            self.timer.stop()
            return

        self.step = self.step + 10
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)
            self.button.setText('Stop')


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
    '''

