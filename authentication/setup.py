import sqlite3, os.path
from signup import signup_screen
from login import login_screen 
from start import start_screen


def startup() -> list: 
    #checking db exists
    if os.path.exists("programme.db") == False:
        connection = sqlite3.connect('programme.db') #db creation
        connection = connection.cursor()
        connection.execute(''' create table users (userID TEXT, username TEXT,password TEXT, private_key TEXT,public_key TEXT)''')
        connection.execute(''' create table messages (timestamp TEXT,senderID TEXT,receiverID TEXT, contents TEXT)''')
        connection.execute(''' create table contacts (alias TEXT, contactID TEXT,userID TEXT, public_key TEXT, wifi_mac_address TEXT, bluetooth_mac_address TEXT)''')
        connection.close()
    
    login:bool = False
    while login == False: #authentication loop
        choice = start_screen() #can return login or signup
        match choice:
            case 'login':
                    login_output = login_screen()
                    if login_output[0] == True:
                        login = True
                        credentials:tuple = login_output[1]
                        (username,password) = credentials
                    else:
                        exit() #5 tries exceeded inside function programme now ends
            case 'signup':
                signup_output = signup_screen()
                if signup_output[0] == True:
                    login = False #can now loop back round to sign in properly
                else:
                    exit() #5 tries exceeded inside function programme now ends    
    return username,password

        
        
        
        
#allows this file to be ran seperately to facilitate testing        
if __name__ == '__main__':
    startup()