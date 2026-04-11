from PySide6.QtWidgets import QMainWindow,QApplication,QMessageBox
from ui_files import loginscreen_ui
from authentication_scripts.resetpw import resetpw_screen
from main_window_scripts import hash_function

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
        self.fail_count:int =0 
        self.credentials:tuple = '',''
        self.success:bool = False

    def closeEvent(self, event)-> None: #handles programme closing properly
        QApplication.instance().quit()
        event.accept()   


    def forgotpassword(self): #displays the reset pw screen hiding the login UI until it has completed
        self.hide()
        resetpw_screen(self.database)
        self.show()
        
        
    def logincheck(self): #linked to login button sees if a successful login attempt has been made
        end_of_check = False #either 5 times exceeded or success
        username = self.ui.username_entry.text()
        password = self.ui.password_entry.text() #getting text from Qlineedits
        hashed_password = hash_function(password)
        if len(username.strip()) ==0 or len(password.strip()) == 0: #checks that they arent empty or just have empty space in
            self.ui.errorlabel.setText('missing field try again')
            self.fail_count +=1
        elif not self.database.loginquery(username,hashed_password): #queries logins in database
            self.ui.errorlabel.setText('invalid credentials')
            self.fail_count +=1
        else:
            self.credentials = (username,password) #adds successful credentials to an attribute to be accessed by the main programme
            self.success = True
            self.close()
        if self.fail_count >=5: #ends the attempt if too many failed ones have been made
            QMessageBox.warning(self,'Fail','Too many failed attempts.')
            self.close()
    
if __name__ == '__main__':
    pass