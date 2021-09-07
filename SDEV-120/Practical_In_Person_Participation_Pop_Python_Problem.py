# Students will be creating a python program that will make use of parallel
# arrays to take in a list of names and how much their food cost. The program
# will add the total of all the foods and devide that by the number of people.
# The program will then tell if each person is above or below the average price
# of food. The requirements for the program:
# 
# * Put the names of people into a list.
# * Take the price of the food for each person into a seperate list.
# * Sum all the food prices together.
# * Tell each user if they are over or under the average and by how much.

import math

def get_cost():
    while True:
        try:
            num = float(input("How much was their meal: "))
            break
        except ValueError:
            print("You did not give a number.")
            continue
    return num

if __name__ == "__main__":
    name = []
    food = []
    another = "y"
    while another != "n":
        name.append(input("What is the name of the person getting food?\n"))
        food.append(get_cost())
        while True:
            another = input("Would you like to add another person?\nY|n: ").lower()
            if another == "y" or another == "" or another == "n":
                break
            else:
                print("Please use a 'y' or an 'n' to continue.")
    
    people = len(name)
    total = sum(food)
    average = total / people
    
    for i, j in zip(name, food):
        diff = average - j
        if diff > 0:
            print(f"{i} is paying ${diff:.2f} below the average price ${average:.2f}")
        elif diff < 0:
            diff = abs(diff)
            print(f"{i} is paying ${diff:.2f} above the average price ${average:.2f}")
