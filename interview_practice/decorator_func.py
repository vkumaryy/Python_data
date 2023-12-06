def my_deco(func):
    def wrapper():
        print("Something is happening befor the function called")
        func()
        print("Something is happening after the function called.")
    return wrapper

@my_deco
def say_hello():
    print("Hello decorator")

say_hello()