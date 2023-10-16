class Dog:
    attr1 = "mammal" 

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

Roger = Dog("Roger")
Tommy = Dog("Tommy")

print("Roger is a {}" .format(Roger.__class__.attr1))
print("Tommy is a {}" .format(Tommy.__class__.attr1))

print(Roger.attr1)

Roger.speak()