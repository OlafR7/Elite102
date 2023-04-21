import mysql.connector
from random import randint

def create_account():
    connection = mysql.connector.connect(user = 'user',database = 'example',password = 'Pass!word')
    cursor = connection.cursor()

    name = input("Enter your name: ")
    u_name = input("Enter a username for your account: ")
    password = input("Enter a password: ")
    pin = randint(1000, 9999)
    add_account = (f"INSERT INTO accounts(name, pin, username, password) VALUES (\"{name}\", {pin}, \"{u_name}\", \"{password}\")")

    cursor.execute(add_account)

    connection.commit()
    cursor.close()
    connection.close()

def login():
    connection = mysql.connector.connect(user = 'user', database = 'example', password = 'Pass!word')
    cursor = connection.cursor()

    u_name = input("Enter your username: ")
    password = input("Enter your password: ")
    get_account = (f'SELECT id, name, pin, balance FROM accounts WHERE username = \"{u_name}\" AND password = \"{password}\"')
    cursor.execute(get_account)
    for item in cursor:
        return(item[0], item[1], item[2], item[3])
            
    cursor.close()
    connection.close()