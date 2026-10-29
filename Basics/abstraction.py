# Makes our code simple..dont use your brains further.

from abc import ABC , abstractmethod

class Mandatory(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Mandatory):
    def __init__(self,radius):
        self.radius = radius

obj = Square(12)

#abstractionmethod makes it mandatory for the class to also specify perimeter and area in its class but thats just one component of abstraction..for now we just know how it works and know how to use abstractmethod..thats enough for now.

