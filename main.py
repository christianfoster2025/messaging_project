from authentication_scripts import login_window,signup_window,start_window
from main_window_scripts import main_window
from core_scripts import databaseinterfacer
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
import sys


def main() -> None:
    runtime = QApplication(sys.argv) #instantiate the application runtime
    runtime.styleHints().setColorScheme(Qt.ColorScheme.Light)
    db = databaseinterfacer() #instantiating the database
    while True: #main programme loop
        start = start_window() #instantiating start UI
        start.show()
        runtime.exec()
        match start.chosen: #choice from whichever button was clicked on the start UI
            case 'login':
                login = login_window(db) #instantiates login UI
                login.show()
                runtime.exec()
                if login.success:
                    username,password = login.credentials #gets credentials from login
                    main = main_window(db,username) #instantiates main programme
                    main.show()
                    main.start_receiver() #starts message receiver thread
                    runtime.exec()
                    if main.end: 
                        break #triggered if the X is clicked on the main screen
                    else:
                        db.close()  #triggered if the signout button is pressed reinstantiating database to clear cache for new login
                        db = ''
                        db = databaseinterfacer()
                    
            case 'signup':
                signup = signup_window(db) #instantiates the signup UI
                signup.show()
                runtime.exec()
        if start.endscript :
            break       #closes programme if close clicked on start page
    db.close()              



if __name__ == "__main__": #entry point for the programme
    main() 
    