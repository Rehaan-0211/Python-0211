# print positive and negative values from a list

a=[10,11,12,14,-2,-2,-5]

print("Positive elements are :- ")
for i in range(len(a)):
    if a[i] >= 0:
        print(a[i])

print("Negative elements are :- ")
for i in a:
    if i < 0:
        print (i) 