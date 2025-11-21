from PySide6.QtWidgets import QMainWindow,QApplication
from main_programme.main_screen import Ui_MainWindow
import sys

class main_window(QMainWindow):
    
    def __init__(self,db):
        super(main_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) #imports ui
        
        
        self.database = db #db link
        
       
                
            
    
def mainscreen(db,userID,username,password):
    runtime = QApplication(sys.argv)
    screen = main_window(db)
    screen.show()
    runtime.exec()
    runtime.shutdown()
    
    
if __name__ == '__main__':
    pass


