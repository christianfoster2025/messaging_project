import hashlib


def hash_function(password:str) -> str: #hashes password
    password = password.encode('ascii')
    output = hashlib.sha256(password) #uses sha256
    output = output.hexdigest() #outputs hash
    output = str(output)
    return output
    
def zerocheck(input:str) -> bool: #lengthcheck
    if len(input) == 0:
        return True
    else: 
        return False
     
     
def encrypt(text:str) -> str: #would encrypt text but unimplemented
    encrypted_text = text
    return encrypted_text 

if __name__ == '__main__':
    pass