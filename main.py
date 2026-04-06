from authentication_scripts import login_window,signup_window,start_window
from main_window_scripts import main_window
from core_scripts import databaseinterfacer
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
import sys


def main() -> None:
    runtime = QApplication(sys.argv) #instantiatie the application runtime
    runtime.styleHints().setColorScheme(Qt.ColorScheme.Light)
    
    #checking db exists
    db = databaseinterfacer()
    
    authenticated:bool = False
    while True: #authentication loop
        start = start_window()
        start.show()
        runtime.exec()
        choice = start.chosen
        match choice:
            case 'login':
                login = login_window(db)
                login.show()
                runtime.exec()
                if login.success:
                    username,password = login.credentials
                    
                    main = main_window(db,username)
                    main.show()
                    main.start_receiver()
                    runtime.exec()
                    if main.end:
                        break
                    else:
                        db.close()  
                        db = ''
                        db = databaseinterfacer()
                    
            case 'signup':
                signup = signup_window(db)
                signup.show()
                runtime.exec()
        if start.endscript :
            break       
                  
    #runtime.shutdown()
    db.close()              



if __name__ == "__main__": #entry point for the programme
    main() 
    