import os, re, socket
from PySide6.QtCore import Signal,QObject

class message_receiver(QObject):
    error = Signal(object)
    newmessage = Signal(str)
    
    def __init__(self):
        super().__init__()
        
    
    def wifi_message_check(self)-> None:
            self.wifi_connection = socket.socket()
            port = 12345
            self.wifi_connection.bind(('', port))
            print ("socket binded to %s" %(port))
            self.wifi_connection.listen(5)    
            print ("socket is listening")
            try:
                while True:
                    # Establish connection with client.
                    c, addr = self.wifi_connection.accept()
                    print(c,addr)
                    #print ('Got connection from', addr )
                    received_text =c.recv(1024).decode('utf-8')
                    
                    #print(f'{addr}: {received_text[2:-1]}')
                    self.newmessage.emit(received_text)
      
            except Exception as e:
                self.error.emit(e)
           
    
    def receiver_close(self)-> None:
        self.wifi_connection.close()   


def send_message(userID,recipientID,contents,db) ->bool:
    #first get mac address from recipient ID
    mac_address = db.get_mac_address(recipientID,userID)
    if mac_address is None:
        return False,'mac address not found'
    # Get the ARP table
    arp_table = os.popen('arp -a').read()
    print(arp_table)
    # Search for the MAC address in the arp table
    for line in arp_table.splitlines():
        print(line)
        if mac_address.lower() in line.lower() or mac_address.lower().replace(':','-') in line.lower():# Extract the IP address from arp table
            
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            print(ip_match)
            if ip_match:
                local_ip_address = ip_match.group()
            
    if not local_ip_address:
        return False,'device not found'
 
    message = (f'{userID}:{contents}').encode('ascii') # attaches userID            
    wifi_connection = socket.socket()
    port = 12345
    try:
        wifi_connection.connect((local_ip_address, port))
        wifi_connection.send(message)
        # close the connection
        wifi_connection.close()
        return True,''
    except ConnectionRefusedError:
        print('client not online')
        return False, 'message failed to send'
    

if __name__ == '__main__':
    pass

    