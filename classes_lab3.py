class str:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
check = str()
check.getString()
check.printString()