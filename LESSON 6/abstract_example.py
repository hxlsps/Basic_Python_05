from abc import ABC, abstractclassmethod

class Polygon(ABC):
    @abstractclassmethod
    def draw(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

class Rectangle(Polygon):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def draw(self):
        print('Draw rectangle')
        
    def get_width(self):
        return self.width

    def get_height(self):
        return self.get_height
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width+self.height)

class Square(Polygon):
    def __init__(self,side):
        self.side=side

    def draw(self):
        print('Draw square')
        
    def get_side(self):
        return self.side
    
    def get_area(self):
        return self.side**2
    
    def get_perimeter(self):
        return 4*self.side 
        
rect_1=Rectangle(3,4)
rect_1.draw()

sq_1=Square(4)
sq_1.draw()

poly_1=Polygon()