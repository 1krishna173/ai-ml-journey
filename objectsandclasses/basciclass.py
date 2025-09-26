# class car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year

# car1=car('Toyota', 'Camry', 2020)
# print(car1.make,car1.model,car1.year)

# class car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#     @staticmethod
#     def start_engine():
#         print("Engine has been started")

# car1=car('Toyota', 'Camry', 2020)
# print(car1.make,car1.model,car1.year)
# car1.start_engine()

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def know(self):
#         print(f"Name of the person is : {self.name},age: {self.age}")
# s1=student("krishna","18")
# s1.know()

# class bank_account:
#     def __init__ (self,accn,bal):
#         self.__accn=accn
#         self.__bal=bal
#     def deposit(self,amount):
#         self.__bal+=amount
#     def withdraw(self,amount):
#         if(amount>self.__bal):
#             print("Insufficient Balance")
#         else:
#             self.__bal-=amount
#     def check_balance(self):
#         return self.__bal

# b=bank_account("1124151080",1000)
# print(b.check_balance())
# b.deposit(200)
# b.withdraw(2000)

class person:
    __name="anonoymous"
    def __hello(self):
        print("Hello")
    def welcome(self):
        self.__hello()
p=person()
print(p.welcome())