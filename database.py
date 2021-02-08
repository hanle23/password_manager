import mysql.connector


def connect():
    try:
        mydb = mysql.connector.connect(
            host='127.0.0.1', user="root", password="admin", database="password_manager")
        return mydb
    except (Exception, mysql.connector.Error) as error:
        print(error)


def store_passwords(password, user_email, username, url, app_name):
    try:
        connection = connect()
        mycursor = connection.cursor()
        query = "INSERT INTO accounts (password, user_email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"
        value = (password, user_email, username, url, app_name)
        mycursor.execute(query, value)
        connection.commit()
    except (Exception, mysql.connector.Error) as error:
        print(error)


def find_password_app_name(app_name):
    # Find password by app_name
    try:
        connection = connect()
        mycursor = connection.cursor()
        query = "SELECT password FROM accounts WHERE app_name = " + app_name + ""
        mycursor.execute(query, app_name)
        connection.commit()
        result = mycursor.fetchone()
        print("Password is: " + result[0])
    except (Exception, mysql.connector.Error) as error:
        print(error)


def find_password_email(user_email):
    # Find password by email
    try:
        connection = connect()
        mycursor = connection.cursor()
        query = "SELECT password FROM accounts WHERE user_email = " + user_email + ""
        mycursor.execute(query, user_email)
        connection.commit()
        result = mycursor.fetchone()
        print("Password is: " + result[0])
    except (Exception, mysql.connector.Error) as error:
        print(error)


def find_password_username(username):
    # Find password by app name
    try:
        connection = connect()
        mycursor = connection.cursor()
        query = "SELECT password FROM accounts WHERE username = " + username + ""
        mycursor.execute(query, username)
        connection.commit()
        result = mycursor.fetchone()
        print("Password is: " + result[0])
    except (Exception, mysql.connector.Error) as error:
        print(error)
