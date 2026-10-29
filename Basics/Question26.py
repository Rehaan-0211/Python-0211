# find mean of all list elements 

a = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for i in range(len(a)):
    sum+=a[i]

print(f"The mean value of given list a is:- {int(sum/len(a))}")


    