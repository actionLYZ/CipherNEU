from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,os

class SelectDialog(QDialog):
    filetext = "liyuanzhi\ntongsiming"

    def __init__(self, parent=None):
        super(SelectDialog, self).__init__(parent)
        self.path = os.getcwd()
        self.initUI()
        self.setWindowTitle("选择")
        self.resize(240, 100)
    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("路径："), 0, 0)
        self.pathLineEdit = QLineEdit()
        self.pathLineEdit.setFixedWidth(200)
        self.pathLineEdit.setText(self.path)
        grid.addWidget(self.pathLineEdit, 0, 1)
        button = QPushButton("更改")
        button.clicked.connect(self.SaveFile)
        grid.addWidget(button, 0, 2)
        buttonBox = QDialogButtonBox()
        buttonBox.setOrientation(Qt.Horizontal)  # 设置为水平方向
        buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).setText('选择')
        buttonBox.button(QDialogButtonBox.Cancel).setText('取消')
        buttonBox.accepted.connect(self.accept)  # 确定
        buttonBox.rejected.connect(self.reject)  # 取消


        grid.addWidget(buttonBox, 2, 1)
        self.setLayout(grid)

    #读取文件
    def GetFile(self):
        openfile = QFileDialog()
        self.path, filetype = openfile.getOpenFileName(self,  
                                    "选取文件",  
                                    "C:/",  
                                    "Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        #self.path=open.getOpenFileName()
        #self.path = open.getExistingDirectory()
        #QFileDialog.getSaveFileName()
        
        print(self.path)
        self.pathLineEdit.setText(self.path)

        document = open(self.path,"r")
        print('文件内容如下：')
        for context in document.readlines():
            print(context) 
        document.close()

    #保存文件
    def SaveFile(self):
        savefile = QFileDialog()
        filepath,filetype= savefile.getSaveFileName(self,  
                                    "文件保存",  
                                    "C:/",  
                                    "Text Files (*.txt)")

        document = open(filepath,"w+")
        document.write(self.filetext)
        document.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SelectDialog()
    if dialog.exec_():
        pass