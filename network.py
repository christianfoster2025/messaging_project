import os, re, socket


def send_message(userID,recipientID,contents,db) ->bool:
    #first get mac address from recipient ID
    mac_address = db.get_mac_address(recipientID,userID)
    if mac_address is None:
        return False
    print(mac_address)
    #next get local ip to send

    # Get the ARP table
    arp_table = os.popen('arp -a').read()
    print(arp_table)
    # Search for the MAC address in the arp table
    for line in arp_table.splitlines():
        print(line)
        if mac_address.lower() in line.lower() or mac_address.lower().replace(':','-') in line.lower():
            # Extract the IP address from arp table
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            print(ip_match)
            if ip_match:
                local_ip_address = ip_match.group()
            else:
                return False,'device not found'
        else:
            return False,'device not found'
    print(local_ip_address)            
    # attaches userID 
    message = (f'{userID}:{contents}').encode('ascii')            
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
    



    