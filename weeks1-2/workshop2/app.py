from banking_pkg import account
# from workshop2.banking_pkg.account import show_balance
# from workshop2.banking_pkg.account import show_balance

def atm_menu():
    print("          === Automated Teller Machine ===          ")
    
    name = input("Enter name to register:")
            
    pin = input("Enter PIN:")
    
    balance = 0
    print(name + " has been registered with a starting balance of $", balance)
    while True:
        print("LOGIN")
        name_to_validate = input("Enter name: ")
        pin_to_validate = input("Enter PIN: ")
        if name_to_validate == name and pin_to_validate == pin:
            print("Login successfull!")
            break
        else:
            print("Invalid credentials!")

    while True:
        print("User: " + name)
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------")
        option = input("Choose an option: ")

        if option == "1":
            account.show_balance(balance)
            
        elif option == "2":
            balance = account.deposit(balance)
            account.show_balance(balance)
            
        elif option == "3":
            balance = account.widthdraw(balance)
            account.show_balance(balance)
            
        elif option == "4":
            print(account.logout(name))
            break
            
        else:
            print("Please selected the right option")

atm_menu()
