class Factory:
    a = 12 # attribute

    def hello(self):
        print("I love me") #method

# print(Factory().a)
# print(Factory().hello())


obj = Factory() # we can access elements from the class using objects and we can make multiple

print(obj.hello())