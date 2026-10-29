# find factorial of any number input

n = int(input("Enter the value to find its factorial:- "))
total = 1

for i in range(n,1,-1):
    total *= i
print(total)
