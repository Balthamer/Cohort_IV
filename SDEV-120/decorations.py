def f1(func):
    def wrapper(*args):
        print("Starting...")
        return func(*args)
    return wrapper

@f1
def f(a):
    print(a)

f('Hello World!')

