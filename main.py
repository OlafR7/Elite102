import mysql.connector
from random import randint
name = ""
pin = 0

connection = mysql.connector.connect(user = 'root',database = 'example',password = 'Cjrules1106*')
cursor = connection.cursor()

response = input("Would you like to log in or sign up(l or s): ")
if response == "s":
    name = input("Enter your name: ")
    pin = randint(1000, 9999)
    add_account = (f"INSERT INTO accounts(name, pin) VALUES (\"{name}\", {pin})")
    cursor.execute(add_account)
    connection.commit()
elif response == "l":
    name = input("Enter your name: ")
    pin = input("Enter your pin: ")