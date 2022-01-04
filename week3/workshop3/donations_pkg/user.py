
def login(database, username, password): 
    if username in database:
        if database[username] == password:
            print("Welcome! ", username)
            return username
        elif database[username] != password:
            print ("Incorrect passoword! ")
            return ""
        else:
            print("Username was not found")
            return ""    
    else:
        if username not in database:
            print("\nUsername not found. Please register:")
            return "" 
        
def register(database, username):
    if username in database:
        print("\nUsername already registered") 
        return username
    
    # task 6