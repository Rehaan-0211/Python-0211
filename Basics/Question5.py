# Aight so we need to find a leap year.

Year = int(input("Input the value of year :- "))

if Year % 400 == 0 :
    print("Its a leap year")
elif Year % 100 == 0:
    print ("Its not a leap year")
elif Year % 4 == 0:
    print("Its a leap year")
else:
    print("Its not a leap year")

