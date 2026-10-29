# find the greatest value and also print its index

a= [1,4,43,2,34,53,6,23,65,345,46,45,35,23]

# a.sort()
# print(a[-1]) okay this logic was nice but we have to do this differently for logic building
largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        index = i

print(f"Your largest number is {largest} and its index is {index}")




