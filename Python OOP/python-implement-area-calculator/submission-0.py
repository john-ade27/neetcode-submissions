import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width = None):
        pi = math.pi

        if not width:
            a = pi * (length ** 2)
            return round(a,2)
        
        return (length * width)

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
