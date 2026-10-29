# class Naruto: # parent class
#     ability = "rasengan"
#     def jutsu():
#         print("Shadow clone jutsu")

# class Boruto(Naruto): # child class inheriting properties and behaviour of its parent class
#     pass
# syntax of inhericance 

class Parent:
    def __init__(self,name):
        self.name = name

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def tellmeyourname(self):
        print(f"If your name is {self.name} let me know. I have info that he is {self.age} years old too")

obj = Child("Rehaan",2)
obj.tellmeyourname()