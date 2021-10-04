from hashlib import md5
from datetime import datetime
from getpass import getpass
from time import sleep
import os

if __name__ == "__main__":

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def timestamp():
        now = datetime.now()
        date = now.strftime('%Y-%m-%d %H:%M:%S')
        return date

    def new_user(name):
        while True:
            clear()
            uName = input("What is your user name going to be?\n")
            pass1 = md5(getpass("What is your password:").encode('UTF-8')).hexdigest()
            pass2 = md5(getpass("Confirm your password:").encode('UTF-8')).hexdigest()
            if pass1 == pass2:
                with open('shadow.txt','a') as fShadow:
                    fShadow.write(f"{uName} {pass1}\n")
                with open('log.txt','a') as fLog:
                    fLog.write(f"{timestamp()}, NEW_USER: {uName} created by: {name}.\n")
                    break
            else:
                clear()
                print("Your passwords did not match")
                sleep(2)
                continue

    def login():
        while True:
            unames = []
            shadows = []
            try:
                with open('shadow.txt','r') as fShadow:
                    for line in fShadow:
                        seperater = line.split()
                        unames.append(seperater[0])
                        shadows.append(seperater[1])
            except FileNotFoundError:
                clear()
                print("No file found, starting for new user.")
                sleep(2)
                new_user("System")
                continue
            clear()
            user = input("What is your user name?\n")
            if user in unames:
                count = 0
                position = unames.index(user)
                while True:
                    count += 1
                    passwd = md5(getpass("Please ener your password:").encode('UTF-8')).hexdigest()
                    if passwd == shadows[position]:
                        print("Logged In")
                        with open('log.txt','a') as fLog:
                            fLog.write(f"{timestamp()}, AUTHENTICATED: {user}\n")
                        return True, user
                    elif count == 3:
                        clear()
                        with open('log.txt','a') as fLog:
                            fLog.write(f"{timestamp()}, LOGIN_FAILURE: Attempted login with user {user}\n")
                        print("Your password did not match, you will need to wait before you can try again.")
                        sleep(10)
                        break
                    else:
                        clear()
                        print("Your password did not match")
                        sleep(2)
                        clear()
            else:
                with open('log.txt','a') as fLog:
                    fLog.write(f"{timestamp()}, NOT_IN_LIST: Attempted login with username not in list.\n")
                    getpass("Please enter your password:")
                    clear()
                    print("Your password did not match")
                    sleep(2)
                    clear()
                    getpass("Please enter your password:")
                    clear()
                    print("Your password did not match")
                    sleep(2)
                    clear()
                    getpass("Please enter your password:")
                    clear()
                    print("Your password did not match, you will need to wait before you can try again.")
                    sleep(10)

    def menu():
        status, user = login()
        while status:
            clear()
            question = input(f"Hello {user}, please make a selection.\n  1. Main Program.\n  2. New User.\n  3. Quit.\nWhat is your selection: ")
            if question == '1':
                main()
            elif question == '2':
                new_user(user)
            elif question == '3':
                quit()
            else:
                print("Invalid Input")

    def main():
        clear()
        print("Hello World!")
        sleep(2)

    menu()
