from random import shuffle as shuf

def mult(quest, ans, ans_list, points):
    abcd = ["A", "B", "C", "D"]
    shuf(ans_list)
    print(quest)
    for i,j in zip(abcd, ans_list):
        print(f"  {i}. {j}")
    while True:
        answer = input("Answer: ").upper()
        if answer in abcd:
            break
        else:
            print("Invalid Entry")
    if abcd.index(answer) == ans_list.index(ans):
        points = points + 1
    return points

def main():
    score = 0
    score = mult("What color is the sky on a nice day?","Blue",["Blue", "Brown", "Green", "Purple"],score)
    score = mult("What color is healthy grass?","Green",["Green", "Brown", "Pink", "Clear"],score)
    score = mult("Which is correct?","This one",["This one", "Nope", "Not this", "Don't even try"],score)
    # Add 7 more questions...
    if score > 8:
        print("You get an A")
    elif score > 7:
        print("You get a B")
    elif score > 6:
        print("You get a C")
    elif score > 5:
        print("You get a D")
    else:
        print("You have failed.You must take the test again")
        main()

if __name__ == "__main__":
    main()
