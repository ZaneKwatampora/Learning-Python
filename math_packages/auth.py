import json
import os


USER_FILE = 'users.json'

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file)
