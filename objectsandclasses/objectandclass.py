#creating a student class where giving name , 3marks as parameter and then returning the average as an result
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Pbject Initalized Successfully")
    def average(self):
        s=sum(self.marks)
        return s/3
    @staticmethod #it is a decorator which allows this to work only in ground level
    def hello():
        print("Hello")
    
s1=student("krishna",[70,80,90])
print(s1.average())
s1.hello()