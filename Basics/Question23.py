# check if a string is a pallindrome using function

def string(s):
    total = "" 
    for i in range(len(s)-1,-1,-1):
        total += s[i]
    if total == s:
        return("The string is a pallindrome")
    else:
        return("The string is not a pallidrome")

n = str(input("Input the value of string :- "))

print(string(n))