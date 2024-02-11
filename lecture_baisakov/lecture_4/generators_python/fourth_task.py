class Numbers:
    def __init__(self, start = 0, end = 0):
        self.__start = start
        self.__end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        cont = self.__start
        self.__start += 1
        
        if cont <= self.__end:
            return cont
        else:
            raise StopIteration
    
    def squares(self) -> int:
        generator = Numbers(self.__start, self.__end)
        for number_of_generator in generator:
            yield number_of_generator ** 200
            
test_gn = Numbers(0, 10)

for i in test_gn.squares():
    print(i)



        