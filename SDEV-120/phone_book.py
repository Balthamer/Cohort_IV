# Make a python program that takes in a person's name, phone number and email and
# saves it on one line to a file named contacts.txt. Have the program be able to
# take in more then one name at a time.

def main()
    question = "y"
    while question != "n":
        name = input("Enter the name to add: ")
        phone = input("Enter their phone number: ")
        email = input("Enter their email: ")
        with open("contacts.txt","a") as file:
            file.write(f"{name} {phone} {email}\n")
        while True:
            question = input("Do you want to add more? Y|n: ")
            if question == "y" or question == "" or question == "n":
                break
            else:
                print("You did not make a correct selection. Please use a 'y' or 'n'.")

if __name__ == "__main__":
    main()
