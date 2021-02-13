from database import store_passwords, find_password_app_name, find_password_email, find_password_username, find_users
import subprocess
from hash_maker import password
from sys import platform


def menu():
    print(('-'*13) + 'MENU' + ('-' * 13))
    print('1. Create new password')
    print('2. Add an existence password')
    print('3. Find a password')
    print('4. Find all information that connected to an email')
    print('Q. Exit')
    print('-'*30)
    return input('Your choice: ').capitalize()


def create():
    print('Please provide the name of the site or app you want to generate a password for')
    app_name = input(": ")
    print('Please provide a simple password for this site')
    plaintext = input(": ")
    passw = password(plaintext, app_name, 12)
    if platform == 'win32':
        subprocess.run('clip.exe', universal_newlines=True,
                       input=passw, shell=True)
    elif platform == 'linux' or platform == 'linux2':
        subprocess.run('xclip', universal_newlines=True,
                       input=passw, shell=True)
    else:
        print('Sorry, OS still not compatible')
        menu()
    print('-'*30)
    print('')
    print('Your password has now been created and copied to your clipboard')
    print('')
    print('-' * 30)
    print("Please provide a user email for this app or site")
    user_email = input(': ')
    print("Please provide a username for this app or site (if applicable)")
    username = input(": ")
    if username == None:
        username = ''
    print("Please paste the url to the site that you are creating the password for")
    url = input(': ')
    store_passwords(passw, user_email, username, url, app_name)
    menu()


def find():
    print('What method do you want to find your password?')
    print('1. By site or app name')
    print('2. By your email')
    print('3. By your username')
    print('4. Go back to menu')
    choice = input("Enter here: ")
    while choice != '4':
        if choice == '1':
            print('Enter the name of the app/site: ')
            app_name = input(": ")
            find_password_app_name(app_name)
            exit()
        if choice == '2':
            print('Enter your email: ')
            user_email = input(": ")
            find_password_email(user_email)
            exit()
        if choice == '3':
            print('Enter your username')
            username = input(": ")
            find_password_username(username)
            exit()
        else:
            choice = menu()


def find_accounts():
    user_email = input(
        'Please provide the email that you want to find information for: ')
    find_users(user_email)
    exit()


def add():
    print('Please type the name of the site or app you want to add a password for')
    app_name = input(": ")
    print('Please type the password of the site')
    password = input(": ")
    print("Please provide a user email for this app or site")
    user_email = input(': ')
    print("Please provide a username for this app or site (if applicable)")
    username = input(': ')
    if username == None:
        username = ''
    print("Please paste the url to the site that you are creating the password for")
    url = input(': ')
    store_passwords(password, user_email, username, url, app_name)
    exit()
