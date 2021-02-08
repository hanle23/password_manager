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
