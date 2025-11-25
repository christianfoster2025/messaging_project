from PySide6.QtWidgets import QMainWindow,QApplication
from ui_files.authentication.start_screen import Ui_MainWindow
import sys

class start_window(QMainWindow): 
    
    def __init__(self):
        super(start_window,self).__init__() #inherits the parent class
        self.ui = Ui_MainWindow() #imports ui from the app
        self.ui.setupUi(self)
        self.ui.choice_login.clicked.connect(lambda: self.choice('login')) # attaches buttons to choice function with the right mode
        self.ui.choice_signup.clicked.connect(lambda: self.choice('signup'))
        self.chosen = ''
        
    def choice(self,option):
            self.chosen = option
            self.close()
                
            
    
def start_screen():
    runtime = QApplication(sys.argv)
    screen = start_window()
    screen.show()
    runtime.exec() #initaties main loop
    runtime.shutdown() # when mainloop is ended kills qapplication
    return screen.chosen
    
if __name__ == '__main__':
    start_screen()