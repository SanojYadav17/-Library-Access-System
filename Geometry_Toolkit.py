class ShapeCalculator:
    def area(self, a=0, b= None):
        if b is None:
            return 3.14 *a * a
        else:
            return a * b
            
calc = ShapeCalculator()
print("Circle area:", calc.area(5))
print("Rectangle area:", calc.area(4,6))
