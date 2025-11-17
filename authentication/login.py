from PySide6.QtWidgets import QMainWindow,QApplication
from authentication.login_screen import Ui_MainWindow
from main_programme.encryption import hasher
import sys

class start_window(QMainWindow):
    
    def __init__(self):
        super(start_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.submit_form.clicked.connect(self.logincheck)
        self.ui.username_entry.text()
        
        self.hashed_password = '' 
        self.fail_count =0 
        self.username = ''
        self.password = '' 
        
        
        
    def logincheck(self):
        self.username = self.ui.username_entry.text()
        self.password = self.ui.password_entry.text()
        self.hashed_password = hasher(self.password)
        print(self.ui.username_entry.text(),self.ui.password_entry.text())
                
            
    
def login_screen():
    runtime = QApplication(sys.argv)
    screen = start_window()
    screen.show()
    runtime.exec()
    runtime.shutdown()
    
if __name__ == '__main__':
    login_screen()


