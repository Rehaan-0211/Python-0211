# check if a number is pallindrome or not

n = int(input("Input a numeric value:- "))
original = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n//=10
if (rev == original):
    print("The given number is a pallidrome")
else:
    print("The given number is not a pallindrome")
