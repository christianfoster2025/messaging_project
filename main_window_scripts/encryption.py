import hashlib


def hasher(password:str) -> str:
    password = password.encode('ascii')
    output = hashlib.sha256(password)
    output = output.hexdigest()
    output = str(output)
    #print(f'hex for {password} is {output}')
    return output
    
def zerocheck(input:str) -> bool:
    if len(input) == 0:
        return True
    else: 
        return False
     
if __name__ == '__main__':
    hasher(input())