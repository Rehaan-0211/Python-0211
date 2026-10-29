
# d ={1:10,2:20,3:30,4:40} # stores value in form of key and values...keys must be unique and values can be same.

# print(d[2])

# # we can inherit values from the dictionary using the key value

# a = (1,2,3,4)
# print(a[0])

# we used to access values from indexes 

# we can perform various operation on dictionary..CRUD > create,update,read and delete

# d = {1:10,2:20,3:30,4:40}

# d[1] = 100 #updating
# d[6] = 60 # creating
# del d[4] # deleting

# print(d) # read


# help(dict) use this to find the methods for dictionary
d = {1:10,2:20,3:30,4:40}

a = d.copy() # shallow copy of d

# if we use a= d it becomes a deep copy that means value of a changes the value of b too and vice versa 

help(dict)




