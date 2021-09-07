if __name__ != "__main__":
    def is_num(question):
        while True:
            try:
                num = int(input(question))
                break
            except ValueError:
                print("You did not give a number.")
                continue
        return num
