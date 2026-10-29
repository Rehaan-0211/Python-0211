# Comprehention is basically writing a loop or if else statement in a single line to escape from indentation like you escape from your responsilbilities
# i am a work in progress and i won't give up

#list comprehention
# even = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]

# print(even)

#dictionary comprehention
# power = {x : x**2 for x in range(10) }

# print(power)

#set comprehention
power = {x**2 for x in range(9)} # same as dictionary but no keys this time

print(power)