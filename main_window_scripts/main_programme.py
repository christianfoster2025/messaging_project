from PySide6.QtWidgets import QMainWindow,QApplication, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
from ui_files.main_window.main_screen import Ui_MainWindow
from main_window_scripts.contact import add_contact_screen
import sys



class main_window(QMainWindow):
    
    def __init__(self,db,username):
        super(main_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #imports ui

        self.ui.exit_button.clicked.connect(self.exit_programme)
        self.ui.send_button.clicked.connect(self.send)
        self.ui.add_contact_button.clicked.connect(self.new_contact_button)
                                                   
        self.database = db #db link
        self.username = username
        self.userID = self.database.current_userID(self.username)
        self.contacts =[]

        self.update_contact_list()
        self.current_contact = ''
        self.main_pane_update()

        

    def new_contact_button(self):
       add_contact_screen(self.database,self.username)
       self.update_contact_list()
   
    def send(self):
        pass
        
    def exit_programme(self):
         exit()
           
    def update_contact_list(self) -> None:
        
        self.scroller = self.ui.Contactlist_scroll
        self.scrollwidget = self.ui.Contactlist_scroll_widget
        self.vertical = QVBoxLayout()
        self.contacts = self.database.getcontacts(self.userID)
        print(self.contacts)
        if self.contacts == False:
            instance = QLabel('No contacts to show here')
            self.vertical.addWidget(instance)    
        else:
            
            for contact in self.contacts:
                instance = QPushButton(contact)
                instance.clicked.connect(lambda:self.change_contact(contact))
                self.vertical.addWidget(instance)
        self.scrollwidget.setLayout(self.vertical)
        self.scroller.setWidget(self.scrollwidget)
       
   
    def main_pane_update(self):
        print(self.current_contact)
        if not(self.contacts):
            self.ui.current_contact.setText('no contacts to see here')
        else:
            self.current_contact=self.contacts[0]        
            self.ui.current_contact.setText(self.current_contact)

   
    
    def change_contact(self,contact) -> None:
        if self.current_contact == contact:
            pass
        else:
            self.current_contact = contact
            self.main_pane_update()
  
    
   
   
   
   
   
      
def mainscreen(db,username,password):
    runtime = QApplication(sys.argv)
    screen = main_window(db,username)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    
    
if __name__ == '__main__':
    pass


