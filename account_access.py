import mysql.connector
from random import randint

def create_account():
    connection = mysql.connector.connect(user = 'root',database = 'example',password = 'Cjrules1106*')
    cursor = connection.cursor()

    name = input("Enter your name: ")
    pin = randint(1000, 9999)
    add_account = (f"INSERT INTO accounts(name, pin) VALUES (\"{name}\", {pin})")


    cursor.execute(add_account)
    connection.commit()
    cursor.close()
    connection.close()

def login():
    connection = mysql.connector.connect(user = 'root', database = 'example', password = 'Cjrules1106*')
    cursor = connection.cursor()

    name = input("Enter your name: ")
    pin = input("Enter your pin: ")
    get_account = (f'SELECT name, pin, balance FROM accounts WHERE name = \"{name}\" AND pin = {pin}')
    cursor.execute(get_account)
    for item in cursor:
        return(item[0], item[1], item[2])
            
    cursor.close()
    connection.close()