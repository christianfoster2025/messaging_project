from authentication.setup import startup
from database import databaseinterfacer
def main() -> None: #main programme runtime, this is the script that will actually be ran
    username:str = ''
    password:str = ''
    userID:str = ''
    db = databaseinterfacer()
    username,password = startup(db)
    
    db.close()
    #end of stage one
    


if __name__ == "__main__":
    main()
