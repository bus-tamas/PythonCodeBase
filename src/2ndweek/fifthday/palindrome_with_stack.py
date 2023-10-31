class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def is_empty(self):
        if not self.items:
            return True
        return False

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def empty_stack(self):
        self.items= []
    
    def peek(self):
        return self.items[-1]
    
    def __str__(self) -> str:
        res = ""
        for item in self.items:
            res += str(item) + " "
        return res[:-1]
    
    def to_string(self):
        return ''.join(map(str, self.items))

    def is_palindrome(self):
        string = self.to_string()
        return string == string[::-1]
    

mystack1 = Stack()
mystack1.push("test")
print(mystack1.is_palindrome())

mystack2 = Stack()
mystack2.push("racecar")
print(mystack2.is_palindrome())
