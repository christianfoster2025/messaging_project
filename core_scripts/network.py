import os, re, socket
from PySide6.QtCore import Signal,QObject

class message_receiver(QObject):
    error = Signal(object) #signals back to main thread
    newmessage = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.running = True
        
    
    def wifi_message_check(self)-> None:
            self.wifi_connection = socket.socket() #receiver socket
            port = 12345
            self.wifi_connection.bind(('', port))
            self.wifi_connection.listen(5)    
            
            try:
                while True:
                    c, addr = self.wifi_connection.accept() #when sender tries to connect automatically connects and receivers data
                    received_text =c.recv(1024).decode('utf-8')
                    self.newmessage.emit(received_text) #sends message to main thread
                    
                    if not self.running:
                        break
      
            except Exception as e:
                self.error.emit(e)
           
    
    def receiver_close(self)-> None: #stops the receiver
        self.running = False
        self.wifi_connection.close()   


def send_message(userID,recipientID,contents,db) ->bool:
    #first get mac address from recipient ID
    mac_address = db.get_mac_address(recipientID,userID)
    if mac_address is None:
        return False,'mac address not found'
    # Get the address lookup table
    arp_table = os.popen('arp -a').read()
    # Search for the MAC address in the arp table
    for line in arp_table.splitlines():
        if mac_address.lower() in line.lower() or mac_address.lower().replace(':','-') in line.lower(): #finds the line with the right macaddress in
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line) #pulls the ip address out the line
            if ip_match:
                local_ip_address = ip_match.group()
            
    if not local_ip_address:
        return False,'device not found'
 
    message = (f'{userID}:{contents}').encode('ascii') # attaches userID            
    wifi_connection = socket.socket() #starts sending socket
    port = 12345
    try:
        wifi_connection.connect((local_ip_address, port)) #connects to receiver
        wifi_connection.send(message) #transmits message
        wifi_connection.close() # close the connection
        return True,''
    except ConnectionRefusedError:
        return False, 'message failed to send'
    

if __name__ == '__main__':
    pass

    