# Filters does the same thing as maps, i.e , access every element of the list and apply operations with a functions but unlike maps, we can filter out values..as its name suggests.

a = [1,2,3,4,5,6,7,8,9,10]

result = filter(lambda x : x % 2 == 0 , a)
print(list(result))

# we can of course use functions separately but using lambda is recommended for best use case.
