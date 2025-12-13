import sqlite3, os.path

class databaseinterfacer():
    
    def __init__(self) -> None:
        if os.path.exists("programme.db") == False:
            print('db doesnt exist creating now')
            self.connector = sqlite3.connect('programme.db') #db creation
            self.interfacer = self.connector.cursor()
            self.interfacer.execute(''' create table users (userID TEXT, username TEXT,password TEXT, private_key TEXT,public_key TEXT)''')
            self.interfacer.execute(''' create table messages (timestamp TEXT,senderID TEXT,receiverID TEXT, contents TEXT)''')
            self.interfacer.execute(''' create table contacts (alias TEXT, contactID TEXT,userID TEXT, public_key TEXT, wifi_mac_address TEXT, bluetooth_mac_address TEXT)''')   
            self.connector.commit()
        else:
            #print('db exists')
            self.connector = sqlite3.connect('programme.db')
            self.interfacer = self.connector.cursor()
        self.userid:str = '' #will be used to keep userid to stop it being called unnecessarily   
            
    def loginquery(self,username:str,hashed_password:str) -> bool: # has failout prevention to prevent failout
        try:
            self.interfacer.execute('SELECT * FROM users WHERE username LIKE ? AND password like ?;',(username,hashed_password))
            self.connector.commit()
            if not self.interfacer.fetchone():
                return False
            else:
                return True
        except:
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
            print(e)
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
                print(e)
        else:
            return self.userid
        
    
    def contact_user_add(self, alias:str, wifi_mac:str, bluetooth_mac:str, contactid:str, current_userid:str,public_key:str) -> bool:
        try:
            self.interfacer.execute('INSERT INTO contacts VALUES (?,?,?,?,?,?)',(alias,contactid,current_userid,public_key,wifi_mac,bluetooth_mac))
            self.connector.commit()
            print('success')
            return True
        except Exception as e:
            print(e)
            return False
            
    def contact_preexist_check(self, alias:str, wifi_mac:str, bluetooth_mac:str, contactid:str, current_userid:str,public_key:str) -> bool:
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
        try:
            self.interfacer.execute('SELECT * FROM CONTACTS WHERE userID LIKE ?',(userID,))
            if not(self.interfacer.fetchone):
                return False
            else:
                return self.interfacer.fetchall()
        except:
            return False
    
    
        
    def close(self) -> None:
        self.interfacer.close()
        
        
    #INSERT INTO users (userID,username,password) \
    #    VALUES (3,'banana','{hashtext('fruit')}')
        



if __name__ == '__main__':
    connection = databaseinterfacer()
    
    #print(connection.signup_user_entry('1','paul','dsfakjsldfkasjfh'))
    #print(connection.loginquery('paul','dsfakjsldfkasjfh'))
    connection.close()