class Shape:
    area = 0
    
    def findArea(self, *args):
        s = 1
        for _ in args:
            s *= _
        self.area = s
        
        return s
    

class Rectangle(Shape):
    def __init__(self, Width, Length):
        self.Width = Width
        self.Length = Length
        
    def findArea(self, *args):
        return super().findArea(self.Width, self.Length)
    

rc = Rectangle(2, 4)
print(rc.findArea())