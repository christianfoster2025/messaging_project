import os, re, socket


def send_message(userID,recipientID,contents,db) ->bool:
    #first get mac address from recipient ID
    mac_address = db.get_mac_address(recipientID,userID)
    if mac_address is None:
        return False
    
    #next get local ip to send

    # Get the ARP table
    arp_table = os.popen('arp -a').read()
    # Search for the MAC address in the ARP table
    for line in arp_table.splitlines():
        if mac_address.lower() in line.lower() or mac_address.lower().replace(':','-') in line.lower():
            # Extract the IP address
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if ip_match:
                local_ip_address = ip_match.group()
                
    #final stage send message
    message = contents.encode('ascii')            
    wifi_connection = socket.socket()
    port = 8008
    try:
        # connect to the server on local computer
        wifi_connection((local_ip_address, port))
        wifi_connection.send(message)

        # close the connection
        wifi_connection.close()
        return True
    except ConnectionRefusedError:
        print('client not online')
        return False
    



    