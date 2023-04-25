from account_access import *
from account_functions import *

using_program = True
in_account = False
account_num = 0
name = ""
pin = 0
balance = 0
while using_program:
    response = input("Would you like to log in, sign up, or quit(l or s or quit): ")
    print()
    if response == "quit":
        print("Thank you for using our product.")
        using_program = False
    elif response == "s":
        create_account()
        print()
    elif response == "l":
        try:
            account_num, name, pin, balance = login()
            print()
            print(f'Account number: {account_num}\nName: {name}\nPin Number: {pin}\nBalance: {balance}')
            print()
            in_account = True
        except:
            print("Sorry, that account doesn't exist.\n")
        while in_account:
            next_response = input("Would you like to deposit money, withdrawl money, check your balance, delete your account, or log out(deposit, withdrawl, balance, delete, leave): ")
            print()
            next_response = next_response.lower()
            if(next_response == 'leave'):
                account_num = 0
                name = ""
                pin = 0
                balance = 0
                print("Successfully logged out.")
                print()
                in_account = False
            elif next_response == 'deposit':
                new_bal = deposit(account_num, balance)
                print()
                balance = new_bal
            elif next_response == 'withdrawl':
                new_bal = withdrawl(account_num, balance)
                print()
                balance = new_bal
            elif next_response == 'balance':
                print(f"Balance: ${balance}")
                print()
            elif next_response == 'delete':
                delete(account_num)
                print()
                account_num = 0
                name = ""
                pin = 0
                balance = 0
                in_account = False
            else:
                print("That isn't a valid option.")
    else:
        print("That isn't a valid option.")
            

        
        
