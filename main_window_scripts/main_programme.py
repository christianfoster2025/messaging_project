from PySide6.QtWidgets import QMainWindow,QApplication, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy 
from PySide6.QtCore import QSize, Qt, QRect
from ui_files.main_window.main_screen import Ui_MainWindow
from main_window_scripts.contact import add_contact_screen
from main_window_scripts.encryption import encrypt
import sys



class main_window(QMainWindow):
    
    def __init__(self,db,username):
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

        #inital screen setup
        self.update_contact_list()
        self.current_contact = 0 #needs fixing
        self.main_pane_update()

        

    def new_contact_button(self):
       add_contact_screen(self.database,self.username)
       self.update_contact_list()
   
    def send(self):
        unencrypted_text = self.ui.message_input.text()
        encrypted_text = encrypt(unencrypted_text)
        print(encrypted_text)
        
        
    def exit_programme(self):
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
                #instance.setObjectName(u"pushButton")
                #instance.setGeometry(QRect(0, 100, 361, 91))
                instance.setMinimumSize(QSize(0, 91))
                instance.setStyleSheet(u'''
                QPushButton::checked{
                    background-color: #ffd2cf;
                }
                QPushButton{
                    
                    
                }''')
                #instance.setCheckable(True) #need finishing
                #instance.setChecked(False)
                
                self.vertical.addWidget(instance)
               
        #self.horizontalSpacer = QSpacerItem(160, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum) #change size policy to (screenheight - 90(len(self.contacts)))
        #self.vertical.addItem(self.horizontalSpacer) #TODO logic needs implementing
        
        self.scrollwidget.setLayout(self.vertical)
        self.scroller.setWidget(self.scrollwidget)
       
   
    def main_pane_update(self):
        #print(self.current_contact)
        if not self.contacts:
            self.ui.current_contact.setText('no contacts to see here')
        else:    
            self.ui.current_contact.setText(self.contacts[self.current_contact][0])

   #change contact is broken when connected to main pane update as this resets it to value 0 needs reworking completely
    
    def change_contact(self,index) -> None:
        print(f'index {index}')
        print(f'current contact{self.current_contact}')
        if self.current_contact == index:
            pass
        else:
            self.current_contact = index
            print(self.current_contact)
            self.main_pane_update()
  
    
   
   
   
   
   
      
def mainscreen(db,username,password):
    runtime = QApplication(sys.argv)
    screen = main_window(db,username)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    
    
if __name__ == '__main__':
    pass


