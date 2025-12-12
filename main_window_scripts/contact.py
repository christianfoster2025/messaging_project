from PySide6.QtWidgets import QMainWindow,QApplication, QDialog
from ui_files.main_window.contact_dialogue import Ui_Dialog
import sys
from encryption import zerocheck
from getmac import get_mac_address

class contact_dialogue(QDialog): 
    
    def __init__(self,db,username):
        super(contact_dialogue,self).__init__() #inherits the parent class
        self.ui = Ui_Dialog() #imports ui from the app
        self.ui.setupUi(self)
        self.user_userID = db.current_userID(username) #needs adding
        self.user_wifi_mac = get_mac_address()
        self.user_bluetooth_mac = None
        self.user_public_key = None
        self.attempts = 0
        self.ui.contact_info.setPlainText(f'Wi-Fi Mac Address: {self.user_wifi_mac} \nBluetooth Mac Address: {self.user_bluetooth_mac} \nPublic Key: {self.user_public_key} \nUserID: {self.user_userID}')
        
        
    def accept(self,db) -> None :
        
        if zerocheck(self.ui.alias_entry) or zerocheck(self.ui.userid_entry) or zerocheck(self.ui.publickey_entry) or \
            zerocheck(self.ui.bluetooth_mac_entry) or zerocheck(self.ui.wifi_mac_entry):
            self.attempts +=1
        # TODO alias check, check all things havent been entered before
        
        else: 
            print('testing accept')
            super().accept()
            
            
        
        
        if self.attempts > 3:
            super().reject()
            
    def reject(self) -> None:
        super().reject()
        
def add_contact_screen(db,username):
    
    dialogue = contact_dialogue(db,username)
    dialogue.show()
    
    result= dialogue.exec_() 
    dialogue.close()
    #initaties main loop
    
    #runtime.shutdown() # when mainloop is ended kills qapplication
    

    
if __name__ == '__main__':
    pass