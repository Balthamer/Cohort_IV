def get_num(question):
    def decorator(func):
        def wrapper():
            while True:
                try:
                    x = int(input(question))
                    return func(x)
                except ValueError:
                    print("That is not a number.")
        return wrapper
    return decorator

@get_num("Please give a posative number: ")
def get_pos(x):
    if x > 0:
        return x
    else:
        print("That is not a positive number")
        return get_pos()

num = get_pos()
print(num)
