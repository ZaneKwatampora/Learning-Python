from register import register
from login import login

def main():
    while True:
        print('\n1. Register\n2. Login\n3. Exit')
        choice = input('Choose an option: ')
        
        if choice == '1':
            register()
        elif choice ==  '2':
            login()
        elif choice == '3':
            print("Goodbye")
            break
        else:
            print('Invalid request')

if __name__ == "__main__":
    main()
            