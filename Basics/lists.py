a = [12,24,45,34.5]

# #to traverse(going through each element one by one..)

# #indexing
# # for i in range(len(a)):
# #     print(a[i])
# # #directly calling its values
# # for i in a:
# #     print(i)

# #lets discuss various methods for lists 
# #append = adds single value at the end of list
a.append(10)
print (a)

# #insert = inserts a value at a provided index
a.insert(1,16)
print (a)

# #extend = adds multiple values at the end of the list
a.extend([15,20,25])
print(a)

# #remove = removes the first occurence of the given element
a.remove(10)
print(a)

# #pop = pops out a value from the list 
# #if pop function is not given any index it gives the last element
a.pop()
print(a)
# #if index its given its gonna be popped out
a.pop(2)
print(a)
# #useful when we need to get a value out of the list and execute it separately

# #index = just finds the index of the element
print(a.index(12))

#count = counts occurences of a element
print(a.count(12))

#sort = sorts the list in an ascending order
a.sort()
print(a)

#reverse = reverses the list order
a.reverse()
print(a)

#copy = copies the elements from a list , useful if we wanna manipulate the list while keeping its values the same
b = a.copy()
print(a,b)

#clear = clears all the values in a list
a.clear()
print(a)

