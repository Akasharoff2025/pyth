class rectangle:
    def  __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print("area",a)
    def perimeter(self):
        p=2*self.length+self.breadth
        print("perimeter",p)
length=int(input("Enter the length"))
breadth=int(input("Enter the breadth"))
obj1=rectangle(length,breadth)
obj1.area()
obj1.perimeter()
