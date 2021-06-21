# Import module
from menu import menu, create, find, find_accounts, add
from database import connect, create_table, table_exist, delete_table

# Import json for saving login information
import json

# Reading Login information if available, if not, create new file


def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Write new user information to json file


def writeUsers(usr):
    with open("users.json", "w+") as f:
        json.dump(usr, f)


# Login function that check password and username
def login(usr):
    print("Welcome back! Please enter your information as follow:")
    print("Type Q at anytime to exit")
    username = input("Username: ")
    if username in usr.keys():
        password = input("Password: ")
        if password == usr[username]:
            print("-"*30)
            print("Welcome back.")
            return True
        elif password == 'Q' or password == 'q':
            exit()
        else:
            print("Incorrect password, please try again.")
            print("-"*30)
            return False
    elif username == 'Q' or username == 'q':
        exit()
    else:
        print("Username is not exist, please try again")
        print("-"*30)
        return False

# Register function for new user, create new "accounts" table


def register(usr):
    print("Hi stranger! Please enter your information as follow:")
    username = input("Username: ")
    password = input("Password: ")
    snd_password = input("Confirming password: ")
    if username in usr.keys():
        print("The account is already exist, please try to login")
        return False
    # Check if database has already exist
    if table_exist:
        print("Data detected, do you still want to process to register and delete old data? (Yes/No)")
        choice = input(": ").capitalize()
        if choice == "Yes":
            delete_table()
            create_table()
        else:
            quit()
    elif not table_exist:
        create_table()

    # Comparing two password
    if password == snd_password:
        usr[username] = password
        writeUsers(usr)
        return True
    else:
        print("Password is not similar, please try again")
        return False

# Change password function for existence user


def change_password(usr):
    print("Type in your information to change password:")
    print("Type Q at anytime to exit")
    username = input("Username: ")
    old_password = input("Password: ")
    if username in usr.keys():
        if old_password == usr[username]:
            new_password = input("New password: ")
            conf_new_password = input("Confirm New Password: ")
            if new_password == conf_new_password:
                usr[username] = new_password
                print("Password change success")
                return True
            else:
                print("New password does not similar")
                return False
        elif old_password == "Q":
            exit()
        else:
            print("Your password is wrong, please try again")
            return False
    elif username == "Q":
        exit()
    else:
        print("Username is unavailable, please try again")
        return False


def main():
    users = readUsers()
    while True:
        print("Please choose from one of the following options")
        print("1. Register as a new user")
        print("2. Login as a returning user")
        print("3. Change password")
        print("Q. Exit")
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
        elif choice == "3":
            success = change_password(users)
            while not success:
                success = change_password(users)
        elif choice == 'Q' or choice == 'q':
            exit()
        else:
            print("Input not valid, please try again. \n")

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
