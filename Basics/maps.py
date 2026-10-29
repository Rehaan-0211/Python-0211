# we can use maps to target every element in a list with the help of a function

def double(x):
    return x*2

listie = [1,2,3,4,5]

result = map(double,listie)
print(list(result))

# its preferred to use maps and filters with lambda functions for best use case.