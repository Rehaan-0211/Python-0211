# bahahaha a decorator is a function which modifies another function without changing the actual code.

def decorate(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorate
def hello(): # this interprets as hello() = decorate(hello) since we use our own decorator
    print("Wassup")

hello()
