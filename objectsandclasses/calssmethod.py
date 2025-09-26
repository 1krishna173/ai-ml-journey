# class person:
#     name='unknown'
#     def __init__(self,name):
#         self.name=name

# p=person("Ram")
# print(p.name,person.name)  #this shows that there are two variable created of name one for the object and the other one is for the class

# class person:
#     name='unkown'
#     def __init__(self,name):
#         person.name=name
   
# p=person("Ram")
# print(p.name,person.name)     


# class person:
#     name='unkown'
#     def __init__(self,name):
#         self.__class__.name=name
   
# p=person("Ram")
# print(p.name,person.name)  

class person:
    name='unkown'
    def __init__(self,name):
        self.name=name
    @classmethod
    def changename(cls,name):
        cls.name=name
   
p=person("Ram")
p.changename("Rahul")#default name  has been changed
print(p.name,person.name)  

