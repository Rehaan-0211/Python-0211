# A type of polymorphism in which basically a child class can override the value of its parent class but it depends on the object which calls them.

class Animal:
    def show(self):
        print("Hey i am an animal rawr")

class Human(Animal):
    def show(self):
        print("Ultimately i am an animal to but i am intelligent...RAWR!")

obj = Animal()
obj.show()

# Here if we input animal with an object as an instance..it simply gives us the value but if we call its child class what happens? The child class overrides the value of its parent. This is method overriding.