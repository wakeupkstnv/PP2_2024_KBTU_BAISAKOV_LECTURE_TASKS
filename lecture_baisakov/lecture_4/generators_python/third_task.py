class DivBy4and3:
    def __init__(self, end):
        self.end = end
    
    def __iter__(self):
        self.start = 0
        return self
    
    def __next__(self):
        cont = self.start
        self.start += 12
        
        if cont <= self.end:
            if cont % 12 == 0:
                return cont
        else:
            raise StopIteration

inter_obj = DivBy4and3(48)
inter_obj = iter(inter_obj)

for i in inter_obj:
    print(i)