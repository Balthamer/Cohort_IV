# Psydocode:
# Get a number from the user
# Compare that number to 10
# If the number is 10, let the user know they are correct
# If the number is less then 10, tell the user they are to low
# If the number is greater then 10, tell the user they are to high
# Tell the user Good Bye at the end of the program

num = int(input("Please enter a number: "))
if num == 10:
    print("Your number is correct.")
elif num < 10:
    print("Your number is tiny.")
else:
    print("Your number is huge.")
print("Goodbye!")
