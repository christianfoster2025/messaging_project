from PySide6.QtWidgets import QMainWindow,QApplication, QDialog
from PySide6.QtCore import Qt
from ui_files.main_window.contact_dialogue import Ui_Dialog
import sys
from main_window_scripts.encryption import zerocheck
from getmac import get_mac_address

class contact_dialogue(QDialog): 
    
    def __init__(self,db,username):
        #UI import
        super(contact_dialogue,self).__init__() #inherits the parent class
        self.ui = Ui_Dialog() #imports ui from the app
        self.ui.setupUi(self)
        self.database = db
        
        #variable init
        self.user_userID = db.current_userID(username)
        self.user_wifi_mac = get_mac_address()
        self.user_bluetooth_mac = None
        self.user_public_key = None
        self.attempts = 0
        
        #screen setup self contact info
        self.ui.contact_info.setPlainText(f'Wi-Fi Mac Address: {self.user_wifi_mac} \nBluetooth Mac Address: {self.user_bluetooth_mac} \nPublic Key: {self.user_public_key} \nUserID: {self.user_userID}')
        self.ui.contact_info.setEnabled(True)    # Must be True to interact
        self.ui.contact_info.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse | 
            Qt.TextInteractionFlag.TextSelectableByKeyboard
            )
        
    def accept(self) -> None :
        #collect fields from UI
        alias=self.ui.alias_entry.text()
        wifi_mac=self.ui.wifi_mac_entry.text()
        bluetooth_mac=self.ui.bluetooth_mac_entry.text()
        contactid=self.ui.userid_entry.text()
        current_userid=self.user_userID
        public_key=self.ui.publickey_entry.text()
        
        #very basic vallidation
        if zerocheck(alias) or zerocheck(wifi_mac) or zerocheck(bluetooth_mac) or \
            zerocheck(contactid) or zerocheck(public_key):
            self.attempts +=1
            self.ui.errorlabel.setText('Please fill all fields.')
            
        # check doesnt exist
        elif self.database.contact_preexist_check(self.user_userID,alias, wifi_mac, bluetooth_mac, contactid,public_key):
            self.attempts += 1
            self.ui.errorlabel.setText('Make sure the contact is unique')
        
        
        else: 
            print('testing accept')
            try:
                self.database.contact_user_add(alias,wifi_mac,bluetooth_mac, contactid, current_userid,public_key)
                super().accept()
                self.close()
            except:
                self.ui.errorlabel.setText('Database error try again.')
        
        if self.attempts > 3: #if fails 3 times ends
            super().reject()
            
    def reject(self) -> None:
        super().reject()
        
def add_contact_screen(db,username):
    dialogue = contact_dialogue(db,username) #instantiation
    dialogue.show()
    result= dialogue.exec() #runtime within main window
    dialogue.close()
   
    

    
if __name__ == '__main__':
    pass