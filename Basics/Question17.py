# check if a string is pallidrome or not

n = str(input("Enter the string value:- "))
total = ""
for i in range(len(n)-1,-1,-1):
    total += n[i]
if(total == n):
    print("Its a pallindrome")
else:
    print("Its not a pallindrome")
