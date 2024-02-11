class EvenNumbers:
    def __init__(self, end):
        self.end = end
        
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter <= self.end:
            out = self.counter
            self.counter += 1

            if out % 2 == 0: 
                return out
            else:
                return self.__next__() 
        else:
            raise StopIteration
    def size(self):
        return self.end
          
    
generator = EvenNumbers(11)
generator = iter(generator)

for index, obj in enumerate(generator):
    if index != int(generator.size() / 2):
        print(f'{obj}', end=", ")
    else:
        print(obj)
