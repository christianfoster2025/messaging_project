from PySide6.QtWidgets import QMainWindow,QApplication
from authentication.start_screen import Ui_MainWindow
import sys

class start_window(QMainWindow):
    
    def __init__(self):
        super(start_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choice_login.clicked.connect(lambda: self.choice('login'))
        self.chosen = ''
        
    def choice(self,option):
            self.chosen = option
            self.close()
                
            
    
def start_screen():
    runtime = QApplication(sys.argv)
    screen = start_window()
    screen.show()
    runtime.exec()
    return screen.chosen
    
if __name__ == '__main__':
    start_screen()