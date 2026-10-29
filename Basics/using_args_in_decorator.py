# lets try

def decorate(func):
    def wrapper(*a,**k):
        print("The addition of your values is:- \n\n")
        func(*a,**k)
        print("We are done now.")
    return wrapper

@decorate
def addition(*a,**k):
    total = 0
    for i in a:
        total += i

    print(f"The sum is :- {total}")

addition(12,456,4334)