class MyClass:
    def __init__(self,name=None) -> None:
        if name is None:
            print("Empty/Default constructor called")
        else:
            self.name = name
            print("parametrized with value",self.name)
    
    def method(self):
        if hasattr(self,"name"):
            print("Method called with name",self.name)
        else:
            print("method without name")

obj1 = MyClass()
obj1.method()

obj2 = MyClass("Tamas")
obj2.method()