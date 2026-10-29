# type of methods which call themselves based on whats specified to be required. If we perform a certain kind of action on an object python understands itself which method has to be called to perform the following operation.

class DunderMethod():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Your name is {self.name} and your age is{self.age}"

    def __add__(self,other):
        sum = 0
        for i in other:
            sum+= i.age

        return f"The sum of your age is {self.age + sum}"

obj = DunderMethod("lion",12)
obj1 = DunderMethod("tiger",23)
obj2 = DunderMethod("bitch", 23)

print(obj + (obj1, obj2))

# sum = 0
#         for i in other:
#             sum += i.age
#         return f"The sum of your age is {self.age + sum}" i used obj1+obj2 bro doesnt even know how to create a fucking tuple..anyways i got my mistake now.
