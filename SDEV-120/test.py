from random import shuffle as shuf
import os

def clear():
    os.system("cls" if os.name == 'nt' else 'clear')

question_list = ["Apple", "Bannana", "Cherry", "Date", "Elderberry", "Fig", "Gundam"]
other_list = ["A", "B", "C", "D", "E", "F", "G"]

clear()
answer = ""
correct = "Gundam"
print("Which one does not fit?")
shuf(question_list)
for letter, fruit in zip(other_list, question_list):
    print(f"  {letter}. {fruit}")
while answer not in other_list:
    answer = input().upper()
if other_list.index(answer) == question_list.index(correct):
    print("Correct")
else:
    print("Wrong!")
