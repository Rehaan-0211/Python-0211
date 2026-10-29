"Calculate the reoccurence of a number from a list w dict"

a = [1,1,1,1,2,2,2,2,3,3,3,3,45,5,5,5,5,6]

dict = {}

for i in a:
    if  i in dict.keys():
        dict[i] +=  1
    else :
        dict[i] = 1

print(dict)