from PySide6.QtWidgets import QMainWindow,QApplication,QDialog, QMessageBox
from PySide6.QtCore import Qt
from ui_files import resetpw_screen_ui
from main_window_scripts.encryption import hash_function
import sys

class resetpw_window(QDialog):
    
    def __init__(self,db):
        
        #screen setup
        super().__init__()
        self.ui = resetpw_screen_ui()
        self.ui.setupUi(self)
        self.ui.submit_form.clicked.connect(self.resetcheck) #connects the button
        self.database = db
        
        #variable setup
        self.confirm_hashed_password = ''
        self.fail_count =0 
        
        
    def resetcheck(self): #linked to button
        username = self.ui.username_entry.text() #takes in user entries
        password = self.ui.password_entry.text()
        confirmpassword = self.ui.confirm_password.text()
        fail = False
        if len(username.strip())==0 or len(password.strip())==0 or len(confirmpassword.strip())==0: #length/whitespace check
            fail = True
            self.ui.errorlabel.setText('missing fields')
        elif password != confirmpassword: #check passwords match
            fail = True
            self.ui.errorlabel.setText('passwords don\'t match')
        elif not(self.database.user_exist_query(str(username))): #checks theres an entry for that user in the database
            fail = True
            self.ui.errorlabel.setText('username not found')
        else:
            hashed_password = hash_function(password)
            if self.database.reset_password(username,hashed_password): #tries to apply password
                self.close() #successful end
            else:
                fail = True
        
        if fail: 
            self.fail_count +=1
        
        if self.fail_count >=5:
            QMessageBox.warning(self,'Too many failed attempts.')
            self.close() #unsuccessful end
        
                
            
    
def resetpw_screen(db):
    screen = resetpw_window(db) #call class
    screen.show() #show window
    screen.exec() #runtime loop


if __name__ == '__main__':
    pass


