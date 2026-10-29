# It helps us to create a function and write certain conditions in a single line of code...basically its comprehention but in a function.
class lambda_function:
    @staticmethod
    def attribute():
        square = lambda x : x**2
        return square(6)
                    
    #We can also use if else statements

    @staticmethod
    def statements():
        even = lambda x : "Even" if x % 2 == 0 else "Odd"
        return even(6)

obj = lambda_function()
print(obj.statements())