class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y
    
def main():
    calc = Calculator()
    
    while True:
        x = input("First number (or 'q' to quit): ")
        if x == 'q':
            with open("log.txt", "r") as log_file:
                log_contents = log_file.read()
                print("Log file contents:")
                print(log_contents)
            break
            
        
        try:
            x = int(x)
            y = int(input("Second number: "))
            
            print("Choose operation: [+ or - or * or /]")
            operation = input(": ")

            if operation not in ['+', '-', '*', '/']:
                print("Invalid input")
                
            if operation == "+":
                result = calc.add(x, y)
            elif operation == "-":
                result = calc.subtract(x, y)
            elif operation == "*":
                result = calc.multiply(x, y)
            elif operation == "/":
                result = calc.divide(x, y)
            
            with open("log.txt", "a") as log_file:
                log_file.write(f"{x} {operation} {y} = {result}\n")

            print("Result:", result)
        
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

