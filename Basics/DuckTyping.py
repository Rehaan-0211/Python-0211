# What does this indicate? well the theory goes like "If it walks and talks like a duck..its a duck" But its confusing if we rely on this theory

class Duck:
    def show(self):
        print("Quack")

class Human:
    def show(self):
        print("Quack?")

# What this theory indicates is that if we have two classes but they carry a same attribute or method with different parameters.. it wont matter cause they are both in different classes and would be called differently...therefore there is no change.

obj = Duck()
obj.show()
