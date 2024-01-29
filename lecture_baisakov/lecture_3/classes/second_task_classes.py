class Shape:
    area = 0
    
    def findArea(self, *args):
        s = 1

        for _ in args:
            s *= _
        self.area = s
        
        return s
    

class Sqare(Shape):
    def __init__(self, Lenght):
        self.Lenght = Lenght
        
    def findArea(self):
        return super().findArea(self.Lenght, self.Lenght)
    

sq = Sqare(3)

print(sq.findArea())



