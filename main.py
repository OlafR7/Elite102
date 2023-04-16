import mysql.connector
from account_access import create_account
from account_access import login


connection = mysql.connector.connect(user = 'root',database = 'example',password = 'Cjrules1106*')
cursor = connection.cursor()
while True:
    response = input("Would you like to log in or sign up(l or s or quit): ")
    if response == "quit":
        print("Thank you for using our product.")
        break
    elif response == "s":
        create_account()
    elif response == "l":
        login()
