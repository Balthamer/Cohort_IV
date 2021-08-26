# Psydocode
# Get a number from the user
# Count from 0 to the user's number by five
# Do not display the number 0
# Tell the user goodbye
num = int(input("Please give me a number: "))
count = 0
while count < num:
    count = count + 5
    print(count)
print("Goodbye~!")
