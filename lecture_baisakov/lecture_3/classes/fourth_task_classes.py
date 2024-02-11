from math import sqrt

class Point:  
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def show(self):
        return self.x, self.y, self.z
    
    def move(self, xn = None, yn = None, zn = None):
        '''
        def move(x, y, z) if we dont want to change this point we took 'None' type
        like move(None, 2, None)
        
        '''
        if xn != None: self.x += xn
        if yn != None: self.y += yn
        if zn != None: self.z += zn
        
    def dist(self, point):
        if type(point) != Point: return None
        '''
        :param: point class

        '''
        return sqrt((point.x ** 2 - self.x ** 2) + (point.y ** 2 - self.y ** 2) + (point.z ** 2 - self.z ** 2))
    

first_point = Point(1, 2, 3)
second_point = Point(2, 3, 4)

print(first_point.show())
first_point.move(None, 3, 4)
print(first_point.show())
print(first_point.dist(second_point))
