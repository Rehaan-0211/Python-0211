# Encapsulation is basically keeping all the data(variables) and code(functions) in a single place - using a class and then basically hide(if needed) the internal details to prevent them from being accessed

class Job:
    def __init__(self,name,age,salary):
        self.name = name # public
        self._age = age # protected (used for name conventions among devs mostly)
        self.__salary = salary # private

obj = Job("Rehaan",20,500000)
print(f"The name of the employee is {obj.name}")
print(f"The age of the employee is {obj._age}")
print(f"Their salary is {obj.__salary}")

# Since we kept the salary as private by using double underscore before its name we cant access or manupulate the value..therefore its private.



