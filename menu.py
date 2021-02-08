from database import store_passwords, find_password_app_name, find_password_email, find_password_username
import subprocess


def menu():
    print(('-'*13) + 'MENU' + ('-' * 13))
    print('1. Create new password')
    print('2. Find a password')
    print('Q. Exit')
    print('-'*30)
    return input('Your choice: ')


# def create():
#     print('Please proivide the name of the site or app you want to generate a password for')
#     app_name = input()
#     print('Please provide a simple password for this site: ')
#     plaintext = input()
#     passw = password(plaintext, app_name, 12)
#     subprocess.run('xclip', universal_newlines=True, input=passw)
#     print('-'*30)
#     print('')
#     print('Your password has now been created and copied to your clipboard')
#     print('')
#     print('-' * 30)
#     user_email = input('Please provide a user email for this app or site')
#     username = input(
#         'Please provide a username for this app or site (if applicable)')
#     if username == None:
#         username = ''
#     url = input(
#         'Please paste the url to the site that you are creating the password for')
#     store_passwords(passw, user_email, username, url, app_name)


def find():
    print('What method do you want to find your password?')
    print('1. By site or app name')
    print('2. By your email')
    print('3. By your username')
    print('4. Go back to menu')
    choice = input("Enter here: ")
    while choice != '4':
        if choice == '1':
            app_name = input()
            find_password_app_name(app_name)
        if choice == '2':
            user_email = input()
            find_password_email(user_email)
        if choice == '3':
            username = input()
            find_password_username(username)
        else:
            choice = menu()
