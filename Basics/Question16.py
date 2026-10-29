# reverse a string without using an in built function

n = str(input("Enter a string value :- "))

for i in range(len(n)-1,-1,-1):
    print(n[i] , end="")
