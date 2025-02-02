class ToUpperCase:
    def getString(self):
        self.st = input("Enter a string: ")
    
    def printString(self):
        print(self.st.upper())
    
st1 = ToUpperCase()
st1.getString()
st1.printString()