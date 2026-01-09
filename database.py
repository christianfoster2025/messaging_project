import sqlite3, os.path, datetime

class databaseinterfacer():
    
    def __init__(self) -> None:
        if os.path.exists("programme.db") == False:
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
            
    def loginquery(self,username:str,hashed_password:str) -> bool: # has failout prevention to prevent failout
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
        
    def signup_user_query(self,username:str) -> bool:
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
           
    def signup_user_entry(self,userID:str,username:str,hashed_password:str) -> bool:
        try:
            self.interfacer.execute('INSERT INTO users VALUES (?,?,?,?,?)',(userID,username,hashed_password,'test','test'))
            self.connector.commit()
            print('success')
            return True
        except Exception as e:
            print(f'signup user entry error:{e}')
            return False
        
    def current_userID(self,username:str) -> str:
        if self.userid == '':
            try:
                self.interfacer.execute('SELECT userID FROM users WHERE username LIKE ?',(username,))
                self.connector.commit()
                #print('success')
                self.userid = self.interfacer.fetchone()
                self.userid = self.userid[0]
                #print(self.userid)
                return self.userid
                
            except Exception as e:
                print(f'current userID fetch error: {e}')
        else:
            return self.userid
        
    
    def contact_user_add(self, alias:str, wifi_mac:str, bluetooth_mac:str, contactid:str, current_userid:str,public_key:str) -> bool:
        try:
            self.interfacer.execute('INSERT INTO contacts VALUES (?,?,?,?,?,?)',(alias,contactid,current_userid,public_key,wifi_mac,bluetooth_mac))
            self.connector.commit()
            #print('success')
            self.contactupdate = True
            return True
        except Exception as e:
            print(f'contact user add error: {e}')
            return False
            
    def contact_preexist_check(self, alias:str, wifi_mac:str, bluetooth_mac:str, contactid:str,public_key:str) -> bool:
        try:
            self.interfacer.execute('SELECT * FROM contacts WHERE alias LIKE ? OR contactID LIKE ? OR public_key LIKE ? OR wifi_mac_address LIKE ? OR bluetooth_mac_address LIKE ?',(alias, wifi_mac, bluetooth_mac, contactid,public_key))
            self.connector.commit()
            if self.interfacer.fetchone():
                return True # present in db so cant continue
            else:
                return False
        except Exception as e:
            print(f'username query error:{e}')
            return True #if fails for any reason will return the result that requires it to be tried again
    
    
    def getcontacts(self,userID:str) -> list:

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
    
    def get_conversations(self,userID,contactID) -> list: #pulls conversations from database in an array with the format [(message,message state),(message,message state)] etc 
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
    
    def store_message(self,userID,contactID,contents,state) -> bool:
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
            print(f'message storing error{e}')
            return False        
        
    def close(self) -> None:
        self.interfacer.close()
        
        
    #INSERT INTO users (userID,username,password) \
    #    VALUES (3,'banana','{hashtext('fruit')}')
        



if __name__ == '__main__':
    #connection = databaseinterfacer()
    pass
    #print(connection.signup_user_entry('1','paul','dsfakjsldfkasjfh'))
    #print(connection.loginquery('paul','dsfakjsldfkasjfh'))
    #connection.close()