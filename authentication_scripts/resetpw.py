from PySide6.QtWidgets import QMainWindow,QApplication,QDialog
from PySide6.QtCore import Qt
from ui_files import resetpw_screen_ui
from main_window_scripts.encryption import hash_function
import sys

class resetpw_window(QDialog):
    
    def __init__(self,db,parent = None):
        
        #screen setup
        super().__init__(parent)
        self.ui = resetpw_screen_ui()
        self.ui.setupUi(self)
        self.ui.submit_form.clicked.connect(self.signupcheck)
        self.database = db
        
        #variable setup
        self.hashed_password = '' 
        self.confirm_hashed_password = ''
        self.fail_count =0 
        self.username = ''
        self.password = ''
        self.confirmpassword = '' 
        self.output:bool = False
        
        
    def signupcheck(self):
        self.username = self.ui.username_entry.text()
        self.password = self.ui.password_entry.text()
        self.confirmpassword = self.ui.confirm_password.text()
        
        
        fail = False
        #print(self.username, len(self.username.strip())==0 )
        if len(self.username.strip())==0 or len(self.password.strip())==0 or len(self.confirmpassword.strip())==0:
            fail = True
            self.ui.errorlabel.setText('missing fields')
        elif self.password != self.confirmpassword:
            fail = True
            self.ui.errorlabel.setText('passwords don\'t match')
            
        elif not(self.database.signup_user_query(str(self.username))):
            fail = True
            self.ui.errorlabel.setText('username not found')
        else:
            print('success')
            self.hashed_password = hash_function(self.password)
            userID = None
            
            if self.database.reset_password(userID,self.username,self.hashed_password):
                self.output = True
                self.close()
            else:
                fail = True
        
        if fail: 
            self.fail_count +=1
        
        if self.fail_count >=5:
            self.close()
        
                
            
    
def resetpw_screen(db):
    runtime = QDialog()
    #runtime.styleHints().setColorScheme(Qt.ColorScheme.Light)
    screen = resetpw_window(db)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    return screen.output


if __name__ == '__main__':
    pass


