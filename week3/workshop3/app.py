# Workshop assignment Week 3
from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, register

database = {"muharem": "zahra20"}
donations = []
authorized_user = ""

while True:
    # show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: ", authorized_user)    
    
    user = int(input("\nPlease Choose From The Following Options: "))

    if user == 1:
        print("\n")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        authorized_user = login(database, username, password)
    elif user == 2:
        username = input("\nPlease enter a username: ")
        password = input("Please enter a password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database["username"] = input("Enter username: ")
            database["password"] = input("Enter password: ")
           
    elif user == 3:
        print("TODO: Write Donate Functionality.")   
    elif user == 4:
        print("TODO: Write Donations Functionality.")   
    elif user == 5:
        print("\nLeaving DonateMe...")
        break
    else:
        print("Incorrect login credentials!")            
        #    stopped on task 5