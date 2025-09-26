class car:
    color='Black'
    @staticmethod
    def start():
        print("The car has started")
    @staticmethod
    def stop():
        print("Car stopped..")
    def __init__(self,type):
        self.type=type
        
class Toyota(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()
        
c1=Toyota("Fortuner","Electric")
c2=Toyota("Prius","DIesel")
print(c1.color)
print(c1.name)
print(c1.start())
print(c1.stop())
    
    