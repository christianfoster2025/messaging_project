from PySide6.QtWidgets import QMainWindow,QApplication
from authentication.signup_screen import Ui_MainWindow
from main_programme.encryption import hasher
import sys

class signup_window(QMainWindow):
    
    def __init__(self,db):
        super(signup_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.submit_form.clicked.connect(self.signupcheck)
        self.database = db
        
        
        self.hashed_password = '' 
        self.confirm_hashed_password = ''
        self.fail_count =0 
        self.username = ''
        self.password = ''
        self.confirmpassword = '' 
        
        
        
    def signupcheck(self):
        self.username = self.ui.username_entry.text()
        self.password = self.ui.password_entry.text()
        self.confirmpassword = self.ui.confirm_password.text()
        
        self.hashed_password = hasher(self.password)
        self.confirm_hashed_password = hasher(self.confirmpassword)
        
        print(''' username: {self.username}
            passwordhash: {self.hashed_password}
            confirm pashwordhash: {self.confirm_hashed_password}  ''')
                
            
    
def signup_screen(db):
    runtime = QApplication(sys.argv)
    screen = signup_window(db)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    
if __name__ == '__main__':
    signup_screen()


