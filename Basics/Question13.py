# print all the factors of a specified number

n = int(input("Insert a value and find its factors:- "))

for i in range(1,n+1):
    if (n % i == 0):
        print(i)
    else:
        continue
