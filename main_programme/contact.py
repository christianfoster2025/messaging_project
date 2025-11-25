from PySide6.QtWidgets import QMainWindow,QApplication
from main_programme.contact_dialogue import Ui_Dialog
import sys
from getmac import get_mac_address

class contact_dialogue(QMainWindow): 
    
    def __init__(self,db,username):
        super(contact_dialogue,self).__init__() #inherits the parent class
        self.ui = Ui_Dialog() #imports ui from the app
        self.ui.setupUi(self)
        self.user_userID = db.current_userID(username) #needs adding
        self.user_wifi_mac = get_mac_address()
        self.user_bluetooth_mac = None
        self.user_public_key = None
        
        self.ui.contact_info.setPlainText(f'Wi-Fi Mac Address: {self.user_wifi_mac} \nBluetooth Mac Address: {self.user_bluetooth_mac} \nPublic Key: {self.user_public_key} \nUserID: {self.user_userID}')
        
        
    def accept(self): pass
    def reject(self): pass        
    
def add_contact_screen(db,username):
    
    dialogue = contact_dialogue(db,username)
    dialogue.show()
    #dialogue.exec() #initaties main loop
    #runtime.shutdown() # when mainloop is ended kills qapplication
 

    
if __name__ == '__main__':
    pass