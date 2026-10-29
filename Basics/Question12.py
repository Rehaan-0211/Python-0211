#Print sum of even and odd numbers separately in a given range

n=int(input("Enter the range :- "))
total1=0
total2=0
for i in range(1,n+1):
    if (i % 2 == 0):
        total1 += i
    else:
        total2 += i
print("Sum of even numbers is",total1,"and Sum of odd numbers is ",total2)

