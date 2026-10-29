# polymorphism is basically a concept in which how we can have same methods or attributes but both of them have different parameters. The way they operate depends on the situation and the object which calls them

def show():
    print("A is greater than B")

def show():
    print("B is greater than A")

show()

# Here, as we can see the second show function is print on the terminal.. this is because it came at the end so it was given the priority thats how python works. And this thing is known as polymorphism.