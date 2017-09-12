
class MainWindow():
    def __init__(self):
        self.loginwindow=None
        self.logedwindow=None
        self.chatwindow=None
    def setWindow(self,loginwindow,chatwindow,logedwindow):
        self.loginwindow=loginwindow
        self.logedwindow=logedwindow
        self.chatwindow=chatwindow


globalWindow=MainWindow()