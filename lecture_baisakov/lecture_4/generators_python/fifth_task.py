class Numbers:
    def __init__(self, start):
        self.start = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        cont = self.start
        self.start -= 1
        
        if cont >= 0:
            return cont
        else:
            raise StopIteration
        

iter_obj = Numbers(10)
iter_obj = iter(iter_obj)

print([_ for _ in iter_obj])