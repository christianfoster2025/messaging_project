from PySide6.QtWidgets import QMainWindow,QApplication
from authentication.login_screen import Ui_MainWindow
from main_programme.encryption import hasher
import sys

class login_window(QMainWindow):
    
    def __init__(self,db):
        super(login_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #imports ui
        
        self.ui.submit_form.clicked.connect(self.logincheck) #connects button
        self.database = db #db link
        
        #variables
        self.hashed_password = '' 
        self.fail_count =0 
        self.username = ''
        self.password = '' 
        self.output = []
        
        
        
    def logincheck(self):
        end_of_check = False #either 5 times exceeded or success
        self.username = self.ui.username_entry.text()
        self.password = self.ui.password_entry.text() #getting text from Qlineedits
        self.hashed_password = hasher(self.password)
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
            self.output = [False]
            
        if end_of_check:
            self.close()
        
        
        
        #print(self.ui.username_entry.text(),self.ui.password_entry.text())
        #print(self.database.loginquery(self.username,self.password))
                
            
    
def login_screen(db):
    runtime = QApplication(sys.argv)
    screen = login_window(db)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    return screen.output()
    
if __name__ == '__main__':
    login_screen()


