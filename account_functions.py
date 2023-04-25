import mysql.connector
import math

def deposit(id, bal):
    amount = input("How much would you like to deposit(No special characters): ")
    try:
        amount = float(amount)
    except:
        print("Sorry, that isn't a number.")
        return bal
    amount = math.floor(amount * 100)/100
    bal = round(float(bal) + amount, 2)
    
    connection = mysql.connector.connect(user = 'user', database = 'example', password = 'Pass!word')
    cursor = connection.cursor()
    
    add_money = (f'UPDATE accounts SET balance = {bal} WHERE id = {id}')
    cursor.execute(add_money)
    print(f'Sucessfully deposited ${amount}.')
    
    connection.commit()
    cursor.close()
    connection.close()
    return bal

def withdrawl(id, bal):
    amount = input("How much would you like to withdrawl(No special characters): ")
    try:
        amount = float(amount)
    except:
        print("Sorry, that isn't a number.")
        return bal
    amount = math.floor(amount * 100)/100
    if float(bal) - amount < 0:
        print("You don't have that much money in your account.")
        return bal
    bal = round(float(bal) - amount, 2)

    connection = mysql.connector.connect(user = 'user', database = 'example', password = 'Pass!word')
    cursor = connection.cursor()

    take_money = (f'UPDATE accounts SET balance = {bal} WHERE id = {id}')
    cursor.execute(take_money)
    print(f'Sucessfully withdrawled ${amount}.')

    connection.commit()
    cursor.close()
    connection.close()
    return bal

def delete(id):
    connection = mysql.connector.connect(user = 'user', database = 'example', password = 'Pass!word')
    cursor = connection.cursor()

    remove_account = (f'DELETE FROM accounts WHERE id = {id}')
    cursor.execute(remove_account)
    print("Account successfully removed.")

    connection.commit()
    cursor.close()
    connection.close()