from PyQt5 import QtWidgets,QtCore  
from Login import Ui_Login
from main import Ui_Form  
from dialog import Ui_dialog
import  time  
    
class MyWindow(QtWidgets.QWidget,Ui_Form):  
    _signal=QtCore.pyqtSignal(str)                         #定义信号,定义参数为str类型  
    def __init__(self):    
        super(MyWindow,self).__init__()  
        self.setupUi(self)  
        self.MyButton.clicked.connect(self.myPrint)  
        self._signal.connect(self.mySignal)               #将信号连接到函数mySignal  
  
    def myPrint(self):  
        self.tb.setText("")  
        self.tb.append("正在打印，请稍候")  
    def mySignal(self,string):  
        print(string)  
        self.tb.append("打印结束")  
 
class SecondWindow(QtWidgets.QWidget,Ui_dialog):
    def __init__(self, parent=None):
        super(SecondWindow,self).__init__()
        self.setupUi(self)


if __name__=="__main__":    
    import sys    
    
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()  
    s=SecondWindow()
    myshow.encrypt.clicked.connect(s.show)

    myshow.show()    
    sys.exit(app.exec_()) 