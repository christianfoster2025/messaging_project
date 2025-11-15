from authentication.setup import startup

def main() -> None: #main programme runtime, this is the script that will actually be ran
    username:str = ''
    password:str = ''
    userID:str = ''
    username,password = startup()
    #end of sstage one
    


if __name__ == "__main__":
    main()
