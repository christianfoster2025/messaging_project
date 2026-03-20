from PySide6.QtWidgets import QMainWindow,QApplication, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QMessageBox,QWidget, QLineEdit
from PySide6.QtCore import QSize, Qt, QRect, Signal,QObject, QThread, QThreadPool, Slot
from ui_files.main_window.main_screen import Ui_MainWindow
from main_window_scripts.contact import add_contact_screen
from main_window_scripts.encryption import encrypt
from network import send_message
import sys,socket,time


class message_receiver(QObject):
    error = Signal(object)
    data = Signal(str)
    newmessage = Signal(bool)
    def __init__(self):
        super().__init__()
        
    
    def wifi_message_check(self)-> None:
            self.wifi_connection = socket.socket()
            port = 12345
            self.wifi_connection.bind(('', port))
            print ("socket binded to %s" %(port))
            self.wifi_connection.listen(5)    
            print ("socket is listening")
            try:
                while True:
                    # Establish connection with client.
                    c, addr = self.wifi_connection.accept()
                    print(c,addr)
                    #print ('Got connection from', addr )
                    received_text =c.recv(1024).decode('utf-8')
                    
                    print(f'{addr}: {received_text[2:-1]}')
                    self.newmessage.emit(received_text)
            except Exception as e:
                self.error.emit(e)
           
    
    def receiver_close(self)-> None:
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
        self.contacts =[] #stores list of tuples with alias and user ids
        self.contact_buttons_dict = {} # stores button objects
        self.contactvert = None

        self.current_contact_index = 0 
        self.current_contact_messages = []
        self.firstrun = True
        
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
        
        if self.database.store_message(self.userID,receiverID,message,state):
            self.ui.message_input.setText('')
        else: 
            QMessageBox.warning(self,'Error','Your Message hasn\'t been saved into the database')
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

            else: 
                QMessageBox.warning(self,'Error: message not stored in database')
        else:
            QMessageBox.warning(self,f'Error: {error} \nPlease try again.')
        
        
    def exit_programme(self) -> None:
         self.stop_receiver()
         time.sleep(1)
         exit()
           
           
           
           
    def update_contact_list(self) -> None:
        
        scroller = self.ui.Contactlist_scroll
        scrollwidget = self.ui.Contactlist_scroll_widget
        if self.firstrun:
        
        
            self.contactvert= QVBoxLayout()
            self.contacts = self.database.getcontacts(self.userID)
            self.contactvert.addStretch()
            if self.contacts == False:
                instance = QLabel('No contacts to show here')
                self.contactvert.addWidget(instance)    
        
        if len(self.contacts) != len(self.contact_buttons_dict):
            while self.contactvert.count():
                item = self.contactvert.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
                #self.contact_buttons_dict[item].takeAt(0)
                #self.contact_buttons_dict[item].deleteLater()
                
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
                self.contactvert.addWidget(instance)
               
        #self.horizontalSpacer = QSpacerItem(160, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum) #change size policy to (screenheight - 90(len(self.contacts)))
        #vertical.addItem(self.horizontalSpacer) #TODO logic needs implementing
        
        scrollwidget.setLayout(self.contactvert)
        scroller.setWidget(scrollwidget)
    

    def main_pane_update(self) -> None:

        if not self.contacts:
            self.ui.current_contact.setText('no contacts to see here')
        else:    
            self.ui.current_contact.setText(self.contacts[self.current_contact_index][0])

            conversation_pull = self.database.get_conversations(self.userID,self.contacts[self.current_contact_index][1]) 
            if conversation_pull == self.current_contact_messages:
                pass
            else:
                scroller = self.ui.messages_scroll
                scrollwidget = self.ui.messages_scroll_widget #needs name change in the .UI file
                vertical = QVBoxLayout()
                self.current_contact_messages = conversation_pull
                if  self.current_contact_messages is None:
                    instance = QLabel('No messages to show here')
                    vertical.addWidget(instance)    
                else:
                    for index in enumerate(self.current_contact_messages):
                        print(index)
                        instance = QLineEdit(str(index[1][0]))
                        instance.setMinimumSize(QSize(0, 91))
                        print(index[1][1])
                        if index[1][1] == 'received':
                            instance.setStyleSheet(u'''
                            background-color:#FFFFFF;
                            ''')
                        else:
                            instance.setStyleSheet(u'''
                            background-color:#4693F5;
                            ''')
                        instance.setReadOnly(True)
                        vertical.addWidget(instance)
            
                scrollwidget.setLayout(vertical)
                scroller.setWidget(scrollwidget)

       

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
    screen.start_receiver()
    runtime.exec()
    runtime.shutdown()
    
    
if __name__ == '__main__':
    pass


