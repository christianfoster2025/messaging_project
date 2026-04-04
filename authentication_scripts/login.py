from PySide6.QtWidgets import QMainWindow,QApplication
from PySide6.QtCore import Qt
from ui_files import loginscreen_ui
from authentication_scripts.resetpw import resetpw_screen
from main_window_scripts import hash_function
import sys

class login_window(QMainWindow):
    
    def __init__(self,db):
        #ui init
        super(login_window,self).__init__()
        self.ui = loginscreen_ui()
        self.ui.setupUi(self) #imports ui
        
        #button connect
        self.ui.submit_form.clicked.connect(self.logincheck) #connects button
        self.ui.reset_password.clicked.connect(self.forgotpassword)
        
        #variables
        self.database = db #db link
        self.hashed_password = '' 
        self.fail_count =0 
        self.username = ''
        self.password = '' 
        self.output = []

    def closeEvent(self, event):
        self.output = []
        return super().closeEvent(event)


    def forgotpassword(self):
        self.hide()
        resetpw_screen(self.database)
        self.show()
        
        
    def logincheck(self):
        end_of_check = False #either 5 times exceeded or success
        self.username = self.ui.username_entry.text()
        self.password = self.ui.password_entry.text() #getting text from Qlineedits
        self.hashed_password = hash_function(self.password)
        if len(self.username.strip()) ==0 or len(self.password.strip()) == 0: #checks that they arent empty or just have empty space in
            self.ui.errorlabel.setText('missing field try again')
            self.fail_count +=1
        credential_check = self.database.loginquery(self.username,self.hashed_password)
        if not credential_check:
            self.ui.errorlabel.setText('invalid credentials')
        else:
            self.output = [True,(self.username,self.password)]
            end_of_check = True
            
        if self.fail_count >=5:
            end_of_check = True
            self.output = ['fail']
            
        if end_of_check:
            self.close()
        
    
def login_screen(db):
    runtime = QApplication(sys.argv)
    runtime.styleHints().setColorScheme(Qt.ColorScheme.Light)
    screen = login_window(db)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    return screen.output
    
if __name__ == '__main__':
    pass