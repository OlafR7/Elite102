from account_access import *
from account_functions import *

in_account = False
account_num = 0
name = ""
pin = 0
balance = 0
while True:
    response = input("Would you like to log in, sign up, or quit(l or s or quit): ")
    if response == "quit":
        print("Thank you for using our product.")
        break
    elif response == "s":
        create_account()
    elif response == "l":
        account_num, name, pin, balance = login()
        print(f'Account_num: {account_num}\nName: {name}\nPin Number: {pin}\nBalance: {balance}')
        while True:
            next_response = input("Would you like to deposit money, withdrawl money, check your balance, delete your account, or log out(deposit, withdrawl, balance, delete, leave): ")
            next_response = next_response.lower()
            if(next_response == 'leave'):
                account_num = 0
                name = ""
                pin = 0
                balance = 0
                print("Successfully logged out.")
                break
            elif next_response == 'deposit':
                new_bal = deposit(account_num, balance)
                balance = new_bal
            elif next_response == 'withdrawl':
                new_bal = withdrawl(account_num, balance)
                balance = new_bal
            elif next_response == 'balance':
                print(f"Balance: {balance}")
            elif next_response == 'delete':
                delete(account_num, pin)
                break
            

        
        
