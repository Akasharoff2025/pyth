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
    def compare_area(self,other_rectagle):
        if self.area() < other_rectangle.area():
            return "The other rectangle has a larger area,"
        else:
            return"Both rectangle have the same area."

rect1=int(input("rect1"))     
length=int(input("Enter the length"))
breadth=int(input("Enter the breadth"))
obj1=rectangle(length,breadth)
obj1.area()
obj1.perimeter()

rect2=int(input("rect2"))     
length=int(input("Enter the length"))
breadth=int(input("Enter the breadth"))

obj2=rectangle(length,breadth)
obj2.area()
obj2.perimeter()
print("Comparison of tw rect")
print(rect1.compare_area(rect2))






