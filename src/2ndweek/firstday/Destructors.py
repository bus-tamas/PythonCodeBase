class Employee:
    def __init__(self):
        print("Employee created")
    
    def __del__(self):
        print("Destructor called")
    
def create_obj():
    obj = Employee()
    return obj
    
obj = create_obj()
print("Program end")