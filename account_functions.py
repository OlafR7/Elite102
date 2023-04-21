import mysql.connector
import math

def deposit(id, bal):
    amount = input("How much would you like to deposit(No special characters): ")
    amount = float(amount)
    amount = math.floor(amount * 100)/100
    bal = float(bal) + amount
    
    connection = mysql.connector.connect(user = 'user', database = 'example', password = 'Pass!word')
    cursor = connection.cursor()
    
    add_money = (f'UPDATE accounts SET balance = {bal} WHERE id = {id}')
    cursor.execute(add_money)
    
    connection.commit()
    cursor.close()
    connection.close()
    return bal

def withdrawl(id, bal):
    amount = input("How much would you like to withdrawl(No special characters): ")
    amount = float(amount)
    amount = math.floor(amount * 100)/100
    if float(bal) - amount < 0:
        print("You don't have that much money in your account.")
        return bal
    bal = float(bal) - amount

    connection = mysql.connector.connect(user = 'user', database = 'example', password = 'Pass!word')
    cursor = connection.cursor()

    take_money = (f'UPDATE accounts SET balance = {bal} WHERE id = {id}')
    cursor.execute(take_money)

    connection.commit()
    cursor.close()
    connection.close()
    return bal

def delete(id):
    connection = mysql.connector.connect(user = 'user', database = 'example', password = 'Pass!word')
    cursor = connection.cursor()

    remove_account = (f'DELETE FROM accounts WHERE id = {id}')
    cursor.execute(remove_account)

    connection.commit()
    cursor.close()
    connection.close()