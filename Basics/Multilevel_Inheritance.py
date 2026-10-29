# Here we have a grandparent -> Parent -> Child where parent inherits the attributes of grandparent class and the child inherits attributes of both classes

class Factory():
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips,color,pockets):
        super().__init__(material, zips,color)
        self.pockets = pockets

reebok = PuneFactory("leather",3,"black",4)

print(reebok.material)

