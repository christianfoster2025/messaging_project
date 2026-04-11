import sqlite3, os.path, datetime

class databaseinterfacer(): #class that handles all interfacing with the database
    
    def __init__(self) -> None:
        if os.path.exists("programme.db") == False: #sees if database exists or not
            print('db doesnt exist creating now')
            self.connector = sqlite3.connect('programme.db') #db creation
            self.interfacer = self.connector.cursor()
            self.interfacer.execute(''' create table users (userID TEXT, username TEXT,password TEXT, private_key TEXT,public_key TEXT)''')
            self.interfacer.execute(''' create table messages (timestamp TEXT,senderID TEXT,receiverID TEXT, contents TEXT, state TEXT)''')
            self.interfacer.execute(''' create table contacts (alias TEXT, contactID TEXT,userID TEXT, public_key TEXT, wifi_mac_address TEXT, bluetooth_mac_address TEXT)''')   
            self.connector.commit()
        else:
            #print('db exists')
            self.connector = sqlite3.connect('programme.db')
            self.interfacer = self.connector.cursor()
            
            
        #caching variables    
        self.userid:str = '' #will be used to keep userid to stop it being called unnecessarily
        self.contactlist:list = [] #cached contact list
        self.contactupdate = False   #tracks if new contact list needs to be pulled down
       
       
       
       
    #===========================================#
    #DATABASE METHOD LAYOUT
    
    #def functionname(variables:type) -> type returned(usually boolean):
    #   try:
    #       main code
    #       if successful:
    #           return True
    #       else: 
    #           return False
    #   except Exception as e:
    #       print(e) outputs the error from the try into the terminal for debugging
    #       return False
    
    #=========================================#
    
       
    def loginquery(self,username:str,hashed_password:str) -> bool: #takes user and passwork and returns true if present in db
        try:
            self.interfacer.execute('SELECT * FROM users WHERE username LIKE ? AND password like ?;',(username,hashed_password))
            self.connector.commit()
            if not self.interfacer.fetchone():
                return False
            else:
                return True
        except Exception as e:
            print(f'login query error:{e}')
            return False
        
    def user_exist_query(self,username:str) -> bool: #takes in username to check if it already has an entry
        try:
            self.interfacer.execute('SELECT * FROM users WHERE username LIKE ?',(username,))
            self.connector.commit()
            if self.interfacer.fetchone():
                return True # present in db so cant continue
            else:
                return False
        except Exception as e:
            print(f'username query error:{e}')
            return True #if fails for any reason will return the result that requires it to be tried again
        
    def reset_password(self,username:str, hashed_password:str) ->bool: # finds the entry with the corresponding username and updates that password
        try:
            userID = self.current_userID(username)
            self.interfacer.execute('UPDATE users SET password = ? WHERE userID LIKE ?',(hashed_password,userID))
            self.connector.commit()
            return True
        except Exception as e:
            print(f'signup user entry error:{e}')
            return False
        
        
    def signup_user_entry(self,userID:str,username:str,hashed_password:str) -> bool: #adds a new user into the database
        try:
            self.interfacer.execute('INSERT INTO users VALUES (?,?,?,?,?)',(userID,username,hashed_password,'test','test'))
            self.connector.commit()
            return True
        except Exception as e:
            print(f'signup user entry error:{e}')
            return False
        
    def current_userID(self,username:str) -> str: #takes the current username and returns its user ID ONLY TO BE USED FOR WHOMEVER IS LOGGED IN CANT BE USED FOR CONTACTS
        if self.userid == '':
            try:
                self.interfacer.execute('SELECT userID FROM users WHERE username LIKE ?',(username,))
                self.connector.commit()
                self.userid = self.interfacer.fetchone()
                self.userid = self.userid[0]
                #print(self.userid)
                return self.userid
                
            except Exception as e:
                print(f'current userID fetch error: {e}')
        else:
            return self.userid
        
    
    def contact_user_add(self, alias:str, wifi_mac:str, bluetooth_mac:str, contactid:str, current_userid:str,public_key:str) -> bool: # adds a new contacts into the database
        try:
            self.interfacer.execute('INSERT INTO contacts VALUES (?,?,?,?,?,?)',(alias,contactid,current_userid,public_key,wifi_mac,bluetooth_mac))
            self.connector.commit()
            self.contactupdate = True
            return True
        except Exception as e:
            print(f'contact user add error: {e}')
            return False
            
    def contact_preexist_check(self,userid:str, alias:str, wifi_mac:str, bluetooth_mac:str, contactid:str,public_key:str) -> bool: #checks to see if any addresses  or ids have been used before for a given user
        try:
            self.interfacer.execute('SELECT * FROM contacts WHERE userID LIKE ? AND (alias LIKE ? OR contactID LIKE ? OR public_key LIKE ? OR wifi_mac_address LIKE ? OR bluetooth_mac_address LIKE ?)',(userid, alias, wifi_mac, bluetooth_mac, contactid,public_key))
            self.connector.commit()
            if self.interfacer.fetchone():
                return True # present in db so cant continue
            else:
                return False
        except Exception as e:
            print(f'username query error:{e}')
            return True #if fails for any reason will return the result that requires it to be tried again
    
    
    def getcontacts(self,userID:str) -> list: #finds all the contacts of a given user and returns as a list

        if self.contactlist == [] or self.contactupdate == True:

            try:
                self.interfacer.execute('SELECT alias,contactID FROM contacts WHERE userID LIKE ?',(userID,))

                self.connector.commit()
                result = self.interfacer.fetchall() # stores result of query in the temp variable result
  
                if not(result): # checks if there are none
                    return []
                else:
                    self.contactupdate = False #sets the flag for retreiving contacts to be false as it has just been done and is therefore up to date
                    self.contactlist = result # returns a list of tuples to be unpacked as needed
                    return self.contactlist
            except Exception as e:
                print(f'get contacts error: {e}')
                return []
        else:
            return self.contactlist
    
    def get_conversations(self,userID,contactID) -> list: #pulls conversations from database in an array with the format [(message,message_state),(message,message_state)] etc 
        try:
            message_list = []
            self.interfacer.execute('SELECT contents,state FROM messages WHERE (senderID LIKE ? AND receiverID LIKE ?) OR (receiverID LIKE ? AND senderID LIKE ?)',(userID,contactID,userID,contactID))

            self.connector.commit()
            result = self.interfacer.fetchall() # stores result of query in the temp variable result

            if not result: # checks if there are none
                return message_list
            else:
                message_list = result # returns a list of tuples to be unpacked as needed
                return message_list
        except Exception as e:
            print(f'get conversations error: {e}')
            return message_list
    
    def store_message(self,userID,contactID,contents,state) -> bool: # puts a new message into the database 
        try:
            if state == 'received':
                senderID = contactID
                receiverID = userID
            else:
                receiverID = contactID
                senderID = userID
            timestamp = str(datetime.datetime.now()).split('.')[0]
            self.interfacer.execute('INSERT INTO messages VALUES (?,?,?,?,?)',(timestamp,senderID,receiverID,contents,state))
            self.connector.commit()
            return True
        except Exception as e:
            print(f'message storing error: {e}')
            return False        
    
    def get_mac_address(self,contactID,userID) -> str: #retreives the mac address of a contact of a user
        try:
            self.interfacer.execute('SELECT wifi_mac_address FROM contacts WHERE userID LIKE ? AND contactID LIKE ?',(userID,contactID))
            self.connector.commit()

            mac_address = self.interfacer.fetchone()
            mac_address= mac_address[0]

            return mac_address
            
        except Exception as e:
            print(f'MAC address fetch error: {e}')
            return None
    
    
        
    def close(self) -> None: #closes the db link
        self.interfacer.close()
    
if __name__ == '__main__':
    pass
