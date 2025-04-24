from auth import load_users
from werkzeug.security import generate_password_hash, check_password_hash


def login ():
    users = load_users()
    username = input("Usernname: ")
    password = input("Password: ")
    
    stored_password = users.get(username)
    if stored_password and check_password_hash(stored_password, password):
        print(f'Login successful, Welcome back {username}')
    else:
        print(f'incorret username or password')