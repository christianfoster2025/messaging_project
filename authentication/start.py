#from PySide6.QtCore import
from PySide6.QtWidgets import QMainWindow,QApplication
from start_screen import Ui_MainWindow
import sys

class start_window(QMainWindow):
    def __init__(self):
        super(start_window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def start_screen():
    runtime = QApplication(sys.argv)
    screen = start_window()
    screen.show()
    
    sys.exit(runtime.exec())
    
if __name__ == '__main__':
    start_screen()