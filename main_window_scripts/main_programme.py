from PySide6.QtWidgets import QMainWindow,QApplication, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QMessageBox
from PySide6.QtCore import QSize, Qt, QThread, Slot
from PySide6.QtGui import QIcon, QPixmap
from ui_files import mainscreen_ui
from main_window_scripts import add_contact_screen,encrypt
from core_scripts import send_message ,message_receiver

class main_window(QMainWindow):
    
    def __init__(self,db,username) -> None:
        super(main_window,self).__init__()
        self.ui = mainscreen_ui()
        self.ui.setupUi(self) #imports ui

        #button connections
        self.ui.exit_button.clicked.connect(self.signout)
        self.ui.exit_button.setText('Sign out')
        self.ui.send_button.setIcon(QIcon(':/send.png'))
        self.ui.send_button.clicked.connect(self.send)
        self.ui.add_contact_button.clicked.connect(self.new_contact_button)
        self.ui.add_contact_button.setIcon(QIcon(':/plus.png'))
        self.ui.add_contact_button.setText('')
                   
        #variable initialisation                                
        self.database = db #db link
        self.username = username
        self.userID = self.database.current_userID(self.username)
        self.end = True #make the programme close when the x is clicked

        #contact UI setup 
        self.contacts =[] #stores list of tuples with alias and user ids
        self.contact_buttons_dict = {} # stores button objects
        self.current_contact_index = 0 
        self.current_contact_messages = []
        self.contact_pane_scroller = self.ui.Contactlist_scroll
        self.contact_pane_scrollwidget = self.ui.Contactlist_scroll_widget
        self.contact_pane_vertical= QVBoxLayout()
        self.firstrun = True

        # main pane setup
        self.main_pane_scroller = self.ui.messages_scroll
        self.main_pane_scrollwidget = self.ui.messages_scroll_widget
        self.main_pane_vertical = QVBoxLayout()
        
        #inital screen setup
        self.update_contact_list()
        self.main_pane_update()
        if self.contacts != []:
            self.current_contact_ID = self.contacts[self.current_contact_index][1]
            self.contact_buttons_dict[self.current_contact_index].setChecked(True)
        else:
            self.current_contact_ID = None
        
        
        
        
   
    def start_receiver(self) -> None: #starts the receiver thread and signal links
        self.threadinstance = QThread()
        self.worker = message_receiver() #instantiats receiver class
        self.worker.moveToThread(self.threadinstance)       
        self.threadinstance.started.connect(self.worker.wifi_message_check) 
        self.worker.newmessage.connect(self.process_incoming_message) #connects signals to functions
        self.worker.error.connect(self.receiver_error)
        self.threadinstance.start() #starts thread

        
    @Slot(object)
    def receiver_error(error:object) -> None: #prints debug errors
       print(error)
       
   
    @Slot(str)    
    def process_incoming_message(self,content:str):
        senderID,message = content.split(':')
        receiverID = self.userID
        state= 'received'
        
        if self.database.store_message(senderID,receiverID,message,state):
            self.main_pane_update()
        else: 
            QMessageBox.warning(self,'Error',f'Your Message, contents: {content} hasn\'t been saved into the database')
         # stores message in db with state 'received'
         #needs to emit a flag that calls for a message panel update


    def new_contact_button(self) -> None: #displays new contact dialogue box and updates ui on close
       add_contact_screen(self.database,self.username)
       self.update_contact_list()
       self.main_pane_update()
       self.contact_buttons_dict[self.current_contact_index].setChecked(True)
  
   
   
    def send(self) -> None: #ingests all information to be sent, sends it, stores message in database
        unencrypted_text = self.ui.message_input.toPlainText()
        if unencrypted_text.isspace() or unencrypted_text.isempty():
            QMessageBox.warning(self,'Error',f'Error: no text entered \nPlease try again.')
        else:
            encrypted_text = encrypt(unencrypted_text) #encrypts text
            recipientID = self.current_contact_ID
            success,error = send_message(self.userID,recipientID,encrypted_text,self.database) #uses network function to send message
            if success:
                state = 'sent'

                if self.database.store_message(self.userID,recipientID,encrypted_text,state): #stores message in db
                    self.ui.message_input.setText('')
                    self.main_pane_update()

                else: 
                    QMessageBox.warning(self,'Error','Error: message not stored in database') #errors displayed as popups
            else:
                QMessageBox.warning(self,'Error',f'Error: {error} \nPlease try again.')
     
    def signout(self):
        self.end = False
        self.close()   
        
    def closeEvent(self, event): #handles closing properly
        self.worker.receiver_close() #stops receiver loop
        QApplication.instance().quit()
        self.worker.thread().quit() #stops thread
        self.worker.thread().wait() #waits until its closed
        event.accept()   #finishes close
           
           
           
           
    def update_contact_list(self) -> None: #sets up the contact pane on the left of the screen
        self.contacts = self.database.getcontacts(self.userID) #pulls current contact list from db
        if self.firstrun: #edge case because only on start of programme can you have 0 contacts, contacts cant be deleted
            self.firstrun = False
            if self.contacts == False:
                instance = QLabel('No contacts to show here')
                self.contact_pane_vertical.addWidget(instance)    
        
        if len(self.contacts) != len(self.contact_buttons_dict): #checks if any contacts have been added, stops if not
            while self.contact_pane_vertical.count():
                item = self.contact_pane_vertical.takeAt(0) #pulls one widget from the pane
                if item.widget():
                    item.widget().deleteLater()#deletes widget
                self.contact_buttons_dict.clear() #clears dict
                
            for index in range (len(self.contacts)): #iterates through the contact list creating a button for each one
                instance = QPushButton(self.contacts[index][0].capitalize())
                #instance.setIcon(QIcon(':/user.png'))

                instance.clicked.connect(lambda checked, indx=index: self.change_contact(indx)) #uses pass by value to set up button to connect to right contact
                instance.setMinimumSize(QSize(0, 91))
                instance.setStyleSheet(u'''
                QPushButton:checked{
                    
                    background-color:#4693F5;
                    color: #ffffff;
                    border: 1px solid #ffffff;
                    border-radius:8px;
                }
                QPushButton:hover{
                    
                    background-color:#e9e9eb;
                    color: #000000;
                    border: 1px solid #ffffff;
                    border-radius:8px;
                
                     
                }
                QPushButton{
                    background-color:#ffffff;
                    color: #000000;
                    border: 1px solid #ffffff; 
                    border-radius:8px;
               
                            
                }''')
                instance.setCheckable(True)
                instance.setChecked(False)
                instance.setIcon(QIcon(':/user.png'))
                
                self.contact_buttons_dict[index] = instance #add to the dictionary so it can be accessed later
                self.contact_pane_vertical.addWidget(instance) #adds to the ui
        self.contact_pane_vertical.addStretch() #groups widgets at top
        self.contact_pane_scrollwidget.setLayout(self.contact_pane_vertical)
        self.contact_pane_scroller.setWidget(self.contact_pane_scrollwidget) #displays
    

    def main_pane_update(self) -> None:
        
        if not self.contacts:
            self.ui.current_contact.setText('No contacts to see here.')
        else:    
            self.ui.current_contact.setText(str(self.contacts[self.current_contact_index][0]).capitalize())

            conversation_pull = self.database.get_conversations(self.userID,self.contacts[self.current_contact_index][1]) #pulls the new messages
            if conversation_pull != self.current_contact_messages: #sees if an update is needed
                while self.main_pane_vertical.count(): #clears the old datata
                    item = self.main_pane_vertical.takeAt(0) #pulls one widget from the pane
                    if item.widget():
                        item.widget().deleteLater()#deletes widget
                    
                
                self.current_contact_messages = conversation_pull #updates the attribute
                if  self.current_contact_messages is None:
                    instance = QLabel('No messages to show here')
                    self.main_pane_vertical.addWidget(instance)    
                else:
                    for index in enumerate(self.current_contact_messages):
                        instance = QLabel(str(index[1][0])) #puts text in message
                        instance.setMinimumWidth(0)
                        instance.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed) 
                        instance.setWordWrap(True) #makes the message as small as possible
                        if index[1][1] == 'received': #uses the read receipts to dicate the colouring of the message bubble, blue sent grey received
                            instance.setStyleSheet(u''' 
                            background-color:#e9e9eb;
                            color: #000000;
                            border: 1px solid #ffffff; 
                            border-radius:8px;
                            padding:4px 8px;
                            ''')
                            self.main_pane_vertical.addWidget(instance,alignment=Qt.AlignmentFlag.AlignLeft) # received messages stack on the left side of the screen and adds to ui
                        else:
                            instance.setStyleSheet(u'''
                            background-color:#4693F5;
                            color: #ffffff;
                            border: 1px solid #ffffff; 
                            border-radius:8px;
                            padding:4px 8px;
                            ''')
                            self.main_pane_vertical.addWidget(instance,alignment=Qt.AlignmentFlag.AlignRight) # sent messages stack on the right side and adds to screen
                self.main_pane_vertical.addStretch() #adds a spacer to keep messages at the top
                self.main_pane_scrollwidget.setLayout(self.main_pane_vertical)
                self.main_pane_scroller.setWidget(self.main_pane_scrollwidget) #adds the panels to the screens

       

    def change_contact(self,index) -> None:

        if self.current_contact_index == index:
            self.contact_buttons_dict[self.current_contact_index].setChecked(True) #set the cureent contact to be highlighted if it hasnt been changed
        else:
            self.contact_buttons_dict[self.current_contact_index].setChecked(False) #unhighlight the old one
            self.current_contact_index = index #update the index
            self.current_contact_ID = self.contacts[self.current_contact_index][1] #update the header
            self.main_pane_update() #update the message panel
   
if __name__ == '__main__':
    pass


