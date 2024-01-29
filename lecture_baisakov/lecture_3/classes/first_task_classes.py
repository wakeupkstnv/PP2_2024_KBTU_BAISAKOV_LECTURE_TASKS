class UseString():
    def getString(self, value):
        self.string = value
        
    def printString(self):
        print(self.string)


first = UseString()
first.getString('Some String')
first.printString()