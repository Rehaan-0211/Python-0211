# find the second greatest largest value

a= [1,4,43,2,34,53,6,23,65,345,46,45,35,23,69]

largest = a[0]
second_largest = 0
index1 = 0
index2 = 0

for i in range(len(a)):
    if a[i] > largest:
        second_largest = largest
        index2 = index1
        largest = a[i] # basically since the previous largest value was over-ridden..therefore now we will have largest value as i and prev largest becomes the new second largest
        index1 = i
    elif second_largest < a[i]:
        second_largest = a[i]
        index2 = i
print(f"The second largest value is {second_largest} with index {index2}")

