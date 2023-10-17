class Base:
    def __init__(self):
        self.a = "JineshPythonClass"
        self__c= "JineshPythonClass"

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Calling provate member of base class")
        #print(self.__c)

obj1= Base()
print(obj1.a)
# print(obj.__c) --> can not be called here

obj2 = Derived()

