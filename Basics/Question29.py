# find out if a list is sorted or not

a = [1,3,5,6,7,8,4]

for i in range (len(a)-1):
    if a[i] < a[i+1]:
        continue
    else :
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")

