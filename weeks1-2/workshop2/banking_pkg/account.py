def show_balance(balance):
    print("The Current Balance is: $", float(balance))
     
def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    balance = balance + amount
    return balance

def widthdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    balance = balance - amount
    return balance
    
def logout(name):
    print("Goodbye", name + "!")