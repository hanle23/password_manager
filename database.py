import mysql.connector

# Function that connect to a offline database


def connect():
    try:
        mydb = mysql.connector.connect(
            host='127.0.0.1', user="root", password="admin", database="password_manager")
        return mydb
    except (Exception, mysql.connector.Error) as error:
        print(error)

# Function that create new database/table


def create_table():
    try:
        connection = connect()
        mycursor = connection.cursor()
        mycursor.execute(
            "CREATE TABLE accounts (password VARCHAR(60), user_email VARCHAR(60), username VARCHAR(60), url VARCHAR(255), app_name VARCHAR(60))")
        connection.commit()
    except (Exception, mysql.connector.Error) as error:
        print(error)

# Function that help checking if there is exist a table


def table_exist():
    table = 'accounts'
    connection = connect()
    mycursor = connection.cursor()
    mycursor.execute("SHOW TABLES")
    connection.commit()
    results = mycursor.fetchone()
    result_list = [item[0] for item in results]
    if table in result_list:
        return True
    else:
        return False

# Delete table function


def delete_table():
    connection = connect()
    mycursor = connection.cursor()
    mycursor.execute("DROP TABLE accounts")
    connection.commit()

# Function that help store information into database


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

# Find password by app_name


def find_password_app_name(app_name):
    try:
        connection = connect()
        mycursor = connection.cursor(buffered=True)
        query = "SELECT password FROM accounts WHERE app_name = %s"
        app = (app_name, )
        mycursor.execute(query, app)
        connection.commit()
        result = mycursor.fetchone()
        if result != None:
            print("Password is: ")
            print(result[0])
        else:
            print("There is no password available for this app/site")

    except (Exception, mysql.connector.Error) as error:
        print(error)

# Find password by email


def find_password_email(user_email):
    try:
        connection = connect()
        mycursor = connection.cursor(buffered=True)
        query = "SELECT password FROM accounts WHERE user_email = %s"
        email = (user_email,)
        mycursor.execute(query, email)
        connection.commit()
        result = mycursor.fetchone()
        if result != None:
            print("Password is: ")
            print(result[0])
        else:
            print("There is no password available for this email")

    except (Exception, mysql.connector.Error) as error:
        print(error)

# Find password by app name


def find_password_username(username):
    try:
        connection = connect()
        mycursor = connection.cursor(buffered=True)
        query = "SELECT password FROM accounts WHERE username = %s"
        user = (username, )
        mycursor.execute(query, user)
        connection.commit()
        result = mycursor.fetchone()
        if result != None:
            print("Password is: ")
            print(result[0])
        else:
            print("There is no password available for this username")

    except (Exception, mysql.connector.Error) as error:
        print(error)

# Find information based on email


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
        if result:
            print('')
            print('RESULT')
            print('')
            for row in result:
                for i in range(0, len(row)-1):
                    print(data[i] + row[i])
            print('-'*30)
        elif not result:
            print("There is no data available for this email")

    except (Exception, mysql.connector.Error) as error:
        print(error)
