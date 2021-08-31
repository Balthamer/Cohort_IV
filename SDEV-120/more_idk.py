# Creat a program that makes a list of the users favorit foods
# The list should be any size that the user wants
# Print out the list for the user

# Favorit Food = ff
# q = question for exiting loop
ff = []
while True:
    q = input("Would you like to add a food to your list? \n Y|n ").lower()
    if q == "y" or q == "":
        ff.append(input("What kind of food do you like "))
    elif q == "n":
        break
    else:
        print("You did not give a y or no")
for i in ff:
    print(i, end=" ")

print("are my favorite foods")
