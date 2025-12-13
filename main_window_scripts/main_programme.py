from PySide6.QtWidgets import QMainWindow,QApplication, QPushButton, 
from PySide6.QtCore import QSize
from ui_files.main_window.main_screen import Ui_MainWindow
from main_window_scripts.contact import add_contact_screen
import sys



class main_window(QMainWindow):
    
    def __init__(self,db,username,userID):
        super(main_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #imports ui
        self.ui.exit_button.clicked.connect(self.exit_programme)
        self.ui.send_button.clicked.connect(self.send)
        self.ui.add_contact_button.clicked.connect(lambda: add_contact_screen(self.database,self.username))
        self.database = db #db link
        self.username = username
        self.userID = userID
        self.contact_widget = []
        self.update_contact_list()

   
    def send(self):
        pass
        
    def exit_programme(self):
         exit()
           
    def update_contact_list(self) -> None:
        print('hello')
        contacts =['test']
        
        contacts = self.database.getcontacts(self.userID)
        if contacts == False:
            contacts = ['No contacts to show']    
        for i in range(len(contacts)):
            self.contact_widget[i] = QPushButton(self.ui.Contactlist_scroll)
            self.contact_widget[i].setText('hello')
            self.contact_widget[i].setObjectName(i)
            self.contact_widget[i].setMaximumSize(QSize(200, 90))
            
            self.ui.Contactlist_scroll.addWidget(self.contact_widget[i])
        
        
        '''
         self.add_contact_button = QPushButton(self.horizontalLayoutWidget_2)
        self.add_contact_button.setObjectName(u"add_contact_button")
        self.add_contact_button.setMaximumSize(QSize(200, 90))
                   
        self.message_input = QTextEdit(self.horizontalLayoutWidget)
        self.message_input.setObjectName(u"message_input")
        font = QFont()
        font.setPointSize(13)
        self.message_input.setFont(font)

        self.send_bar.addWidget(self.message_input)
'''
    
def mainscreen(db,userID,username,password):
    runtime = QApplication(sys.argv)
    screen = main_window(db,username,userID)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    
    
if __name__ == '__main__':
    pass


