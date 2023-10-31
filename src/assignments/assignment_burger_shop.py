# implement the classes listed below 
class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Burger(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)
class Drink(FoodItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
class Side(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)
class Combo(FoodItem):
    def __init__(self, burger, side, drink):
        name = f"Combo: {burger.name}, {side.name}, {drink.name}"
        price = burger.price + side.price + drink.price
        super().__init__(name, price)
class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_order(self):
        if not self.items:
            print(f"Thank you for considering Burger Shop, {self.customer_name}!")
        else:
            print(f"Order Details for {self.customer_name}:")
            for item in self.items:
                print(f"{item.name}: ${item.price:.2f}")
            total_price = sum(item.price for item in self.items)
            print(f"Total Price: ${total_price:.2f}")
            print(f"Thank you for your order, {self.customer_name}!")
 
def user_input_burger():
    print("Choose a burger:\n1. Hamburger - $2.99\n2. Small Burger - $1.99\n3. Veggie Burger - $2.49")
    
    choice = input("Enter the number of your choice (1/2/3): ")

    if choice == '1':
        b = Burger("Hamburger", 2.99)
    elif choice == '2':
        b = Burger("Small Burger", 1.99)
    elif choice == '3':
        b = Burger("Veggie Burger", 2.49)
    else:
        print("Invalid choice. Please select a valid option.")
        return user_input_burger()

    return b
 
def user_input_drink():
    print("Choose a drink:\n1. Small Soda - $1.49\n2. Medium Soda - $1.99\n3. Large Soda - $2.49\n4. Water - $0.99")
    
    choice = input("Enter the number of your choice (1/2/3/4): ")

    if choice == '1':
        d = Drink("Small Soda", 1.49, "Small")
    elif choice == '2':
        d = Drink("Medium Soda", 1.99, "Medium")
    elif choice == '3':
        d = Drink("Large Soda", 2.49, "Large")
    elif choice == '4':
        d = Drink("Water", 0.99, "Regular")
    else:
        print("Invalid choice. Please select a valid option.")
        return user_input_drink()

    return d
 
def user_input_side():
    print("Choose a side:\n1. Fries - $2.49\n2. Onion Rings - $3.49\n3. Salad - $3.99")
    
    choice = input("Enter the number of your choice (1/2/3): ")

    if choice == '1':
        s = Side("Fries", 2.49)
    elif choice == '2':
        s = Side("Onion Rings", 3.49)
    elif choice == '3':
        s = Side("Salad", 3.99)
    else:
        print("Invalid choice. Please select a valid option.")
        return user_input_side()

    return s
 
def user_input_combo():
    print("Create a Combo:")
    burger = user_input_burger()
    side = user_input_side()
    drink = user_input_drink()
    c = Combo(burger, side, drink)
    return c
 
def take_order():
    #ask user for name for the order 
    #repeat taking order until client is done 
    #display order details
    #display a thank you message
    print("Welcome to Burger Shop")
    customer_name = input("Please enter your name: ")
    order = Order(customer_name)
 
    while True:
        print("Choose: Burger [1] / Side [2] / Drink [3] / Combo [4] / Cancel Order [5] / Done Ordering [6]")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            item = user_input_burger()
        elif choice == '2':
            item = user_input_side()
        elif choice == '3':
            item = user_input_drink()
        elif choice == '4':
            item = user_input_combo()
        elif choice == '5':
            print("Order canceled")
            return
        elif choice == '6':
            break
        else:
            print("Invalid choice. Choose something else.")
            continue

        order.add_item(item)

    order.display_order()

take_order()

