import sqlite3, os.path
from authentication.signup import signup_screen
from authentication.login import login_screen 
from authentication.start import start_screen


def startup(db) -> list: 
    #checking db exists
    
    login:bool = False
    while login == False: #authentication loop
        choice = start_screen() #can return login or signup
        match choice:
            case 'login':
                    login_output = login_screen(db)
                    if login_output[0] == True:
                        login = True
                        credentials:tuple = login_output[1]
                        (username,password) = credentials
                    else:
                        exit() #5 tries exceeded inside function programme now ends
            case 'signup':
                signup_output = signup_screen(db)
                if signup_output == True:
                    login = False #can now loop back round to sign in properly
                else:
                    exit() #5 tries exceeded inside function programme now ends    
    return username,password

        
        
        
        
#allows this file to be ran seperately to facilitate testing        
if __name__ == '__main__':
    startup()