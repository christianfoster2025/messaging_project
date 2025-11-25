from PySide6.QtWidgets import QMainWindow,QApplication
from main_programme.main_screen import Ui_MainWindow
from main_programme.contact import add_contact_screen
import sys



class main_window(QMainWindow):
    
    def __init__(self,db,username):
        super(main_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #imports ui
        self.ui.exit_button.clicked.connect(self.exit_programme)
        self.ui.send_button.clicked.connect(self.send)
        self.ui.add_contact_button.clicked.connect(self.add_contact)
        self.database = db #db link
        self.username:str = username
    
    
    def add_contact(self):
        add_contact_screen(self.database,self.username)
    
    def send(self):
        pass
        
    def exit_programme(self):
         exit()
           
                
            
    
def mainscreen(db,userID,username,password):
    runtime = QApplication(sys.argv)
    screen = main_window(db,username)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    
    
if __name__ == '__main__':
    pass


