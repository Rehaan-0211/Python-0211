# Take an integer and check wheather its an even number or odd number

num = int(input("Input a number :- "))
if num % 2 == 0:
    print("The particular number specified is even")
elif num % 2 != 0:
    print("The particular number specified is odd")
else :
    print("Invalid input please try again")