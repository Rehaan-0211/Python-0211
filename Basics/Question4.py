# Take the name and age of the user and check wheater they are eligible to vote or not

name = str(input("Please input your full name:- "))
age = int(input("Specify your age:- "))

if age >= 18:
    print("Congratulations! You are eligible to vote")

elif age < 18:
    print("You are unfortunately not eligible to vote")
else :
    print("Invalid input please try again.")