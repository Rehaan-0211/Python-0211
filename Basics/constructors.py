class Factory:
    def __init__(self,materials,zips,pockets):
        self.materials = materials
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"The material you are using is {self.materials} with zips = {self.zips} and pockets = {self.pockets}")

    @classmethod
    def class_method(cls):
        print("What's up")

    @staticmethod
    def static_method():
        print("I serve mo one")

reebok = Factory("leather",2,4)

# reebok.show()


reebok.class_method()

print(reebok.materials)