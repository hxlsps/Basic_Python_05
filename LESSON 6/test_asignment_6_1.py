import math
class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
class Triangle(Shape):
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def area(self):
        p = (self.side_1+self.side_2+self.side_3)
        return math.sqrt(p*(p-self.side_1)*(p-self.side_2)*(p-self.side_3))

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width*self.length

def main():
    tri_1 = Triangle(3,4,5)
    print(f'{tri_1.area():.2f}')
    rec_1 = Rectangle(3,4)
    print(rec_1.area())

main()