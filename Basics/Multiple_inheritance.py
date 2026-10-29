# this consists of two parents but one child... and that one child can inherit attributes of both parents

class Parent1:
    def __init__(self,name):
        self.name = name

class Parent2:
    def __init__(self, name2, classes):
        self.name = name2
        self.classes = classes

class Child(Parent1,Parent2): # whatever class we take here as first the initialization function will work for the one which is specified first and foremost..in this case its Parent1.
    
    name3 = "Shivam"

obj = Child("Tinki")
print(obj.name3)
