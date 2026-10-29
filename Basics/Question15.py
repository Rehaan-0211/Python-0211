# check if a number is prime or not

n = int(input("Input a value to check if its prime or not:- "))
if(n == 1):
    print("Neither prime nor composite")
if(n == 2 ):
    print("Its a prime number")
# if(n == 3):
#     print("Its a prime number")

for i in range(2,n):
    if (n % i == 0):
        print("Its a composite number")
        break
    else :
        print("Its a prime number")
