class Bird:
    def intro(self):
        print("There are many types of birds")
    
    def fly(self):
        print("Most of the birds can fly but some cannot")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")

obj_bird = Bird()
obj_sparrow = Sparrow()
obj_ostrich = Ostrich()

obj_bird.intro()
obj_bird.fly()

obj_sparrow.intro()
obj_sparrow.fly()

obj_ostrich.intro()
obj_ostrich.fly()