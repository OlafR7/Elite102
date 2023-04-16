import mysql.connector
from account_access import *

in_account = False
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
        name, pin, balance = login()
        print(f'Name: {name}\nPin Number: {pin}\nBalance: {balance}')
        while True:
            next_response = input("Would you like to deposit money, withdrawl money, delete your account, or log out(deposit, withdrawl, delete, leave): ")
            next_response = next_response.lower
            if(next_response == 'leave'):
                print("Successfully logged out.")
                break
            elif next_response == 'deposit':
                print('not done')
            elif next_response == 'withdrawl':
                print('not done')
            elif next_response == 'delete':
                print('not done')
            

        
        
