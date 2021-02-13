from menu import menu, create, find, find_accounts, add
import json
from database import connect


def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def writeUsers(usr):
    with open("users.json", "w+") as f:
        json.dump(usr, f)


def login(usr):
    print("Welcome back! Please enter your information as follow:")
    username = input("Username: ")
    password = input("Password: ")
    if username in usr.keys():
        if password == usr[username]:
            print("-"*30)
            print("Welcome back.")
            return True
        else:
            print("Incorrect password.")
            return False


def register(usr):
    print("Hi stranger! Please enter your information as follow:")
    username = input("Username: ")
    connection = connect()
    mycursor = connection.cursor()
    mycursor.execute(
        "CREATE TABLE accounts (password VARCHAR(60), user_email VARCHAR(60), username VARCHAR(60), url VARCHAR(255), app_name VARCHAR(60))")
    connection.commit()
    password = input("Password: ")
    snd_password = input("Confirming password: ")
    if password == snd_password:
        usr[username] = password
        writeUsers(usr)
        return True
    else:
        print("Password is not similar, please try again")
        return False


def main():
    users = readUsers()
    print("Please choose from one of the following options")
    print("1. Register as a new user")
    print("2. Login as a returning user")
    print("-----------------------------")
    choice = input(": ")
    if choice == "1":
        success = register(users)
        while not success:
            success = register(users)
    elif choice == "2":
        success = login(users)
        while not success:
            success = login(users)
    choice = menu()
    while choice != 'Q':
        if choice == '1':
            create()
        elif choice == '2':
            add()
        elif choice == '3':
            find()
        elif choice == '4':
            find_accounts()
        else:
            choice = menu()

    exit()


if __name__ == "__main__":
    main()
