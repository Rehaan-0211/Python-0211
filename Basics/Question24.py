# The upcoming questions are related to lists

# find all even and odd numbers from a list

a = [10,11,12,13,14,15,16,17,18,19,120]
even = 0
odd = 0

for i in a:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1

print(f"In case of the given list a, the number of even numbers in the list are {even} and the no of odd numbers present in the list are {odd}")
