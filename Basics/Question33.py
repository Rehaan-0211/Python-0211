"Combine two dictionaries and then add values in common key values"

d1 = {1:10,2:20,3:30,4:40}
d2 = {4:30,5:50,6:60}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)
print(d2)