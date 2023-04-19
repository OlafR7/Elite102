import mysql.connector
from decimal import Decimal

def deposit(id, bal):
    amount = input("How much would you like to deposit(No special characters): ")
    amount = float(amount)
    amount = round(amount, 2)
    bal = float(bal) + amount
    
    connection = mysql.connector.connect(user = 'root', database = 'example', password = 'Cjrules1106*')
    cursor = connection.cursor()
    
    add_money = (f'UPDATE accounts SET balance = {amount} WHERE id = {id}')
    cursor.execute(add_money)
    
    connection.close()
    cursor.close()
    connection.close()
    return bal

def withdrawl(id, balance):
    print("hello")

def delete(id, pin):
    print("hello")