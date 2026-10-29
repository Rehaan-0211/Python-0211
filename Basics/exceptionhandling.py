# a = int(input("Enter a number :- "))
# try:
#     print(100/a)

# except Exception as err:
#     print(f"sorry you encountered an error - {err}")

# else:
#     print("Good for you no exception encountered")

# finally:
#     print("I'll run anyway nw gng")

# print("Code excecuted successfully")

age = int(input("Input your age sir:- "))

if age < 10 or age >18:
    raise ValueError("Age must be between 10 and 18")
else:
    print("Welcome to the club")

print("The club will start soon")

