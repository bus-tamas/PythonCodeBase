def testmethod(self):
    print("this is test class")

class Base:
    def myfun(self):
        print("This is inherited method")

#create test class dynammically using typ() method
Test = type('Test', (Base,), dict(x="Jinesh",my_method=testmethod))

print(type(Test))

test_obj = Test()
print(type(test_obj))
test_obj.myfun()

test_obj.my_method()
print(test_obj.x)


#Account = type('Account', (Base,), dict(x="Jinesh",my_method=testmethod))
