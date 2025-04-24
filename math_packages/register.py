from auth import load_users, save_users
from werkzeug.security import generate_password_hash, check_password_hash


def register():
    users = load_users()
    username = input('Choose username: ')
    if username in users:
        print('username exists')
    
        return

    password = input('Input a password: ')
    hashed_password = generate_password_hash(password)
    users[username] = hashed_password
    save_users(users)
    print("registered successfully!")