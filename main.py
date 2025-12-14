from authentication_scripts.setup import startup
from main_window_scripts.main_programme import mainscreen
from database import databaseinterfacer



def main() -> None: #main programme runtime, this is the script that will actually be ran
    username:str = ''
    password:str = ''
    userID:str = ''
    db = databaseinterfacer()
    username,password = startup(db)
    
    
    
    
    
    
    mainscreen(db,username,password)
    
    
    
    db.close()
    
    print('stage one completed')
    #end of stage one
    


if __name__ == "__main__":
    main()
    