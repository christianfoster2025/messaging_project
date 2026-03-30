from PySide6.QtWidgets import QMainWindow,QApplication, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QMessageBox,QWidget, QLineEdit
from PySide6.QtCore import QSize, Qt, QRect, Signal,QObject, QThread, QThreadPool, Slot
from PySide6.QtGui import QIcon, QPixmap
from ui_files import mainscreen_ui
from main_window_scripts import add_contact_screen,encrypt
from core_scripts import send_message ,message_receiver
import sys,time

class main_window(QMainWindow):
    
    def __init__(self,db,username) -> None:
        super(main_window,self).__init__()
        self.ui = mainscreen_ui()
        self.ui.setupUi(self) #imports ui

        #button connections
        self.ui.exit_button.clicked.connect(self.exit_programme)
        self.ui.send_button.setIcon(QIcon(':/send.png'))
        self.ui.send_button.clicked.connect(self.send)
        self.ui.add_contact_button.clicked.connect(self.new_contact_button)
                   
        #variable initialisation                                
        self.database = db #db link
        self.username = username
        self.userID = self.database.current_userID(self.username)

        #contact stuff
        self.contacts =[] #stores list of tuples with alias and user ids
        self.contact_buttons_dict = {} # stores button objects
        self.contact_pane_vertical = None
        self.current_contact_index = 0 
        self.current_contact_messages = []
        
        #contact UI setup
        self.contact_pane_scroller = self.ui.Contactlist_scroll
        self.contact_pane_scrollwidget = self.ui.Contactlist_scroll_widget
        self.contact_pane_vertical= QVBoxLayout()
        self.firstrun = True

        #contact pane setup
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
        
        
        
        
   
    def start_receiver(self) -> None:
        self.thread = QThread()
        self.worker = message_receiver()
        self.worker.moveToThread(self.thread)       
        self.thread.started.connect(self.worker.wifi_message_check) 
        self.worker.newmessage.connect(self.process_incoming_message)
        self.worker.error.connect(self.receiver_error)
        self.thread.start() 
   
    def stop_receiver(self)-> None:
        
        self.thread.terminate()
        #will need some extra work not functioning properly
        
    @Slot(object)
    def receiver_error(error:object) -> None:
       print(error)
       
   
    @Slot(str)    
    def process_incoming_message(self,content:str):
        print(content)
        senderID,message = content.split(':')
        receiverID = self.userID
        state= 'received'
        
        if self.database.store_message(senderID,receiverID,message,state):
            self.main_pane_update()
        else: 
            QMessageBox.warning(self,'Error',f'Your Message, contents: {content} hasn\'t been saved into the database')
         # stores message in db with state 'received'
         #needs to emit a flag that calls for a message panel update


    def new_contact_button(self) -> None:
       add_contact_screen(self.database,self.username)
       self.update_contact_list()
   
  
   
   
    def send(self) -> None:
        unencrypted_text = self.ui.message_input.toPlainText()
        encrypted_text = encrypt(unencrypted_text)
        recipientID = self.current_contact_ID
        success,error = send_message(self.userID,recipientID,encrypted_text,self.database)
        if success:
            state = 'sent'

            if self.database.store_message(self.userID,recipientID,encrypted_text,state):
                self.ui.message_input.setText('')
                self.main_pane_update()

            else: 
                QMessageBox.warning(self,'Error: message not stored in database')
        else:
            QMessageBox.warning(self,'Error',f'Error: {error} \nPlease try again.')
        
        
    def exit_programme(self) -> None:
         self.stop_receiver()
         time.sleep(0.2)
         exit()
           
           
           
           
    def update_contact_list(self) -> None:
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
                
            for index in range (len(self.contacts)): #iterates through the contact list
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
                    color: #0;
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
                self.contact_buttons_dict[index] = instance
                self.contact_pane_vertical.addWidget(instance)
        self.contact_pane_vertical.addStretch() #groups widgets at top
        self.contact_pane_scrollwidget.setLayout(self.contact_pane_vertical)
        self.contact_pane_scroller.setWidget(self.contact_pane_scrollwidget) #displays
    

    def main_pane_update(self) -> None:
        
        if not self.contacts:
            self.ui.current_contact.setText('No contacts to see here.')
        else:    
            self.ui.current_contact.setText(str(self.contacts[self.current_contact_index][0]).capitalize())
           #self.ui.current_contact.setPixmap(QPixmap(':/user.png').scaled(24,24))

            conversation_pull = self.database.get_conversations(self.userID,self.contacts[self.current_contact_index][1]) 
            if conversation_pull != self.current_contact_messages:
                while self.main_pane_vertical.count():
                    item = self.main_pane_vertical.takeAt(0) #pulls one widget from the pane
                    if item.widget():
                        item.widget().deleteLater()#deletes widget
                    
                
                self.current_contact_messages = conversation_pull
                if  self.current_contact_messages is None:
                    instance = QLabel('No messages to show here')
                    self.main_pane_vertical.addWidget(instance)    
                else:
                    for index in enumerate(self.current_contact_messages):
                        print(index)
                        instance = QLabel(str(index[1][0]))
                        #instance.setMinimumSize(QSize(0, 91))
                        instance.setMinimumWidth(0)
                        instance.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
                        #instance.setReadOnly(True)
                        instance.setWordWrap(True)
                        print(index[1][1])
                        if index[1][1] == 'received':
                            instance.setStyleSheet(u'''
                            background-color:#e9e9eb;
                            color: #000000;
                            border: 1px solid #ffffff; 
                            border-radius:8px;
                            padding:4px 8px;
                            ''')
                            self.main_pane_vertical.addWidget(instance,alignment=Qt.AlignmentFlag.AlignLeft)
                        else:
                            instance.setStyleSheet(u'''
                            background-color:#4693F5;
                            color: #ffffff;
                            border: 1px solid #ffffff; 
                            border-radius:8px;
                            padding:4px 8px;
                            ''')
                            self.main_pane_vertical.addWidget(instance,alignment=Qt.AlignmentFlag.AlignRight)
                self.main_pane_vertical.addStretch()
                self.main_pane_scrollwidget.setLayout(self.main_pane_vertical)
                self.main_pane_scroller.setWidget(self.main_pane_scrollwidget)

       

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
    runtime.styleHints().setColorScheme(Qt.ColorScheme.Light)
    screen = main_window(db,username)
    screen.show()
    screen.start_receiver()
    runtime.exec()
    runtime.shutdown()
    

if __name__ == '__main__':
    pass


