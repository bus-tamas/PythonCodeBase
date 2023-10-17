class Person:
    def __init__(self, name, age, salary=None):
        self.name = name
        self.age = age
        self.__salary = salary

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))

    def __str__(self):
        return "{} is {} years old.".format(self.name, self.age)
    
    def __repr__(self):
        return "REPR : {} is {} years old.".format(self.name, self.age)

class VIP(Person):
    def __init__(self, name, age, salary=None):
        super().__init__(name, age, salary)

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Status: VIP")

    def __str__(self):
        return "{} is {} years old and has a VIP status".format(self.name, self.age)

# Tests:
p1 = Person("Zac", 33, 3000)
p2 = Person("Max", 25)

p1.display()
p2.display()
print(p1)
print(p2)
print([p1])
print([p2])

try:
    print(p1.__salary)
except:
    print("Salary attribute can not be reached like this.")

vip1 = VIP("Alex",24,2000)
vip2 = VIP("Andrea",20,2500)

print(vip1)
print(vip2)
vip1.display()
vip2.display()

