from PySide6.QtWidgets import QMainWindow,QApplication
from PySide6.QtCore import Qt
from ui_files import signupscreen_ui
from main_window_scripts.encryption import hash_function
import sys, uuid

class signup_window(QMainWindow):
    
    def __init__(self,db):
        
        #screen setup
        super(signup_window,self).__init__()
        self.ui = signupscreen_ui()
        self.ui.setupUi(self)
        self.ui.submit_form.clicked.connect(self.signupcheck)
        self.database = db
        
        #variable setup
        self.fail_count =0 
        self.output:bool = False
        
        
    def signupcheck(self):
        username = self.ui.username_entry.text() #take in user entries
        password = self.ui.password_entry.text()
        confirmpassword = self.ui.confirm_password.text()
        
        fail = False
       
        if len(username.strip())==0 or len(password.strip())==0 or len(confirmpassword.strip())==0: #length/whitespace check
            fail = True
            self.ui.errorlabel.setText('Missing fields')
        elif password != confirmpassword: #checking passwords match
            fail = True
            self.ui.errorlabel.setText('Passwords don\'t match')
            
        elif self.database.user_exist_query(username): #checking user doesn't already exist
            fail = True
            self.ui.errorlabel.setText('This username is already in use')
        else:
            hashed_password = hash_function(password) 
            userID = str(uuid.uuid1())
            if self.database.signup_user_entry(userID,username,hashed_password): #putting user into db
                self.output = True
                self.close()
            else:
                self.ui.errorlabel.setText('Database entry failed, try again')
        
        if fail: 
            self.fail_count +=1
        
        if self.fail_count >=5:
            self.close()

    def closeEvent(self, event): #makes UI closes handle properly so runtime can be passed onto the next UI
        QApplication.instance().quit() 
        event.accept()   
                
if __name__ == '__main__':
    pass


