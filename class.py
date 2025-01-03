class student:
    studentcount=0
    def  __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        student.studentcount += 1
    def displaycount(self):
        print("Total students:",student.studentcount)
    def display_details(self):
        print("Rollno",self.roll)
        print("Name",self.name)
        print("Course",self.course)
student1= student(10,"Jose","MCA")
student1.display_details()
