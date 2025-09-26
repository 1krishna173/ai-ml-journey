class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(f"{self.real}i+{self.img}j")
    def __add__(self,num):
        realnew=self.real+num.real
        imgnew=self.img+num.img
        return Complex(realnew,imgnew)

num1=Complex(2,4)
num2=Complex(3,7)
num3=num1.add(num2)
num3=num1+num2
num1.show()
num2.show()
num3.show()