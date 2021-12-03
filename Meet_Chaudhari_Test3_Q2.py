class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getarea(self):
        return (self.length * self.width)

    def getperimeter(self):
        return 2* (self.length + self.width)

length = int(input("ENTER THE LENGTH:"))
width = int(input("ENTER THE WIDTH:"))
Range = Rectangle (length , width)

print("The area of rectangle is ", Range.getarea())
print("The perimeter of rectangle is ", Range.getperimeter())