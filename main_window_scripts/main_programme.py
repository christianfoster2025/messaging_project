from PySide6.QtWidgets import QMainWindow,QApplication, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QMessageBox 
from PySide6.QtCore import QSize, Qt, QRect, Signal,QObject
from ui_files.main_window.main_screen import Ui_MainWindow
from main_window_scripts.contact import add_contact_screen
from main_window_scripts.encryption import encrypt
from network import send_message
import sys
import socket 

class message_receiver(QObject):
    def __init__(self):

        self.message_inbound = Signal(str)
        self.wifi_connection = ''
    
    def wifi_message_check(self):
            self.wifi_connection = socket.socket()
            port = 8008
            self.wifi_connection.bind(('', port))
            print ("socket binded to %s" %(port))
            self.wifi_connection.listen(5)    
            print ("socket is listening")

            while True:
                # Establish connection with client.
                c, addr = self.wifi_connection.accept()
                print(c,addr)
                #print ('Got connection from', addr )
                received_text =str(c.recv(1024))
                
                print(f'{addr}: {received_text[2:-1]}')
                self.message_inbound.emit(received_text)
                
    
    def receiver_close(self):
        self.wifi_connection.close()    



class main_window(QMainWindow):
    
    def __init__(self,db,username) -> None:
        super(main_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #imports ui

        #button connections
        self.ui.exit_button.clicked.connect(self.exit_programme)
        self.ui.send_button.clicked.connect(self.send)
        self.ui.add_contact_button.clicked.connect(self.new_contact_button)
                   
        #variable initialisation                                
        self.database = db #db link
        self.username = username
        self.userID = self.database.current_userID(self.username)
        self.contacts =[]
        self.contact_buttons_dict = {}

        self.current_contact_index = 0
        self.current_contact_messages = []

        #inital screen setup
        self.update_contact_list()
        self.main_pane_update()

        self.current_contact_ID = self.contacts[self.current_contact_index][1]
        
        #message receive setup
        message_checker = message_receiver()
        message_checker.wifi_message_check()
        message_checker.message_inbound.connect(self.process_incoming_message)
        
        
    def process_incoming_message(self,content):
        ...
        

    def new_contact_button(self) -> None:
       add_contact_screen(self.database,self.username)
       self.update_contact_list()
   
   
   
   
    def send(self) -> None:
        unencrypted_text = self.ui.message_input.text()
        encrypted_text = encrypt(unencrypted_text)
        recipientID = self.current_contact_ID
        if send_message(self.userID,recipientID,encrypted_text,self.database):
            state = 'sent'

            if self.database.store_message(self.userID,recipientID,encrypted_text,state):
                self.ui.message_input.setText('')

            else: 
                QMessageBox.warning(self,'Error','Your Message hasn\'t been saved into the database')
        else:
            QMessageBox.warning(self,'Error','Your Message hasn\'t successfully sent. Please try again.')
        
        
    def exit_programme(self) -> None:
         exit()
           
           
           
           
    def update_contact_list(self) -> None:
        
        self.scroller = self.ui.Contactlist_scroll
        self.scrollwidget = self.ui.Contactlist_scroll_widget
        self.vertical = QVBoxLayout()
        
        for i in reversed(range(self.vertical.count())): 
            self.vertical.itemAt(i).widget().setParent(None) #BROKEN NEEDS FIXING TODO, WIDGETS DO NOT CLEAR 

        self.contacts = self.database.getcontacts(self.userID)
        print(self.contacts)
        if self.contacts == False:
            instance = QLabel('No contacts to show here')
            self.vertical.addWidget(instance)    
        else:
            
            for index in range (len(self.contacts)):
                print(index)
                instance = QPushButton(self.contacts[index][0])
                instance.clicked.connect(lambda checked, indx=index: self.change_contact(indx))
                instance.setMinimumSize(QSize(0, 91))
                instance.setStyleSheet(u'''
                QPushButton::checked{
                    background-color: #ffd2cf;
                }
                QPushButton{
                    
                    
                }''')
                instance.setCheckable(True)
                instance.setChecked(False)
                self.contact_buttons_dict[index] = instance
                self.vertical.addWidget(instance)
               
        #self.horizontalSpacer = QSpacerItem(160, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum) #change size policy to (screenheight - 90(len(self.contacts)))
        #self.vertical.addItem(self.horizontalSpacer) #TODO logic needs implementing
        
        self.scrollwidget.setLayout(self.vertical)
        self.scroller.setWidget(self.scrollwidget)
    
    
    def message_panel_setup(self) -> None:
        self.scroller = self.ui.messages_scroll
        self.scrollwidget = self.ui.scrollAreaWidgetContents #needs name change in the .UI file
        self.vertical = QVBoxLayout()

        if self.database.get_conversations(self.userID,self.contacts[self.current_contact_index][1]) is None:
            ...
    
       
   
    def main_pane_update(self) -> None:

        if not self.contacts:
            self.ui.current_contact.setText('no contacts to see here')
        else:    
            self.ui.current_contact.setText(self.contacts[self.current_contact_index][0])


    def change_contact(self,index) -> None:

        if self.current_contact_index == index:
            self.contact_buttons_dict[self.current_contact_index].setChecked(True)
        else:
            self.contact_buttons_dict[self.current_contact_index].setChecked(False)
            self.current_contact_index = index
            self.current_contact_ID = self.contacts[self.current_contact_index][1]
            self.main_pane_update()
  
    
   
   
   
   
   
      
def mainscreen(db,username,password) -> None:
    runtime = QApplication(sys.argv)
    screen = main_window(db,username)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    
    
if __name__ == '__main__':
    pass


