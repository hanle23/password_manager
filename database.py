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
        mycursor = connection.cursor(buffered=True)
        query = "SELECT password FROM accounts WHERE app_name = %s"
        app = (app_name, )
        mycursor.execute(query, app)
        connection.commit()
        result = mycursor.fetchone()
        print("Password is: ")
        print(result[0])
    except (Exception, mysql.connector.Error) as error:
        print(error)


def find_password_email(user_email):
    # Find password by email
    try:
        connection = connect()
        mycursor = connection.cursor(buffered=True)
        query = "SELECT password FROM accounts WHERE user_email = %s"
        email = (user_email,)
        mycursor.execute(query, email)
        connection.commit()
        result = mycursor.fetchone()
        print("Password is: ")
        print(result[0])
    except (Exception, mysql.connector.Error) as error:
        print(error)


def find_password_username(username):
    # Find password by app name
    try:
        connection = connect()
        mycursor = connection.cursor(buffered=True)
        query = "SELECT password FROM accounts WHERE username = %s"
        user = (username, )
        mycursor.execute(query, user)
        connection.commit()
        result = mycursor.fetchone()
        print("Password is: ")
        print(result[0])
    except (Exception, mysql.connector.Error) as error:
        print(error)


def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ')
    try:
        connection = connect()
        mycursor = connection.cursor(buffered=True)
        query = "SELECT * FROM accounts WHERE user_email = %s"
        email = (user_email, )
        mycursor.execute(query, email)
        connection.commit()
        result = mycursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row)-1):
                print(data[i] + row[i])
        print('-'*30)
    except (Exception, mysql.connector.Error) as error:
        print(error)
