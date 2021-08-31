# for life

my_list = []
yes_list = ["y", "Y", "Yes", "yes", "sure", "ok", "why not", ""]
no_list = ["n", "no", "N", "NO", "Oh Hell no"]
while True:
    question = input("Add another:\nY|n: ").lower()
    if question in yes_list:
        my_list.append(input("Give me a friend's name: "))
    elif question in no_list:
        break
    else:
        print("You did not give a y or n")

for i in my_list:
    print(i + " is my friend!")
