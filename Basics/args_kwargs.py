# args and kwargs are type of special keywords which allow functions to accept a flexible number of arguments

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)

# addition(23,3245,342,34,64,744,34,435) positional arguments are passed through args.

def information(**kwargs):
    print("Your information is\n\n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")
    

information(name = "Rehaan" , age = 21 , designation = "data scientist" , salary = 40000)

