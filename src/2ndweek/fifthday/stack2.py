class Stack:
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop() if not self.isEmpty() else -1
    def isEmpty(self):
        return len(self.stack) == 0
    def peek(self):
        return self.stack[-1] if not self.isEmpty() else -1
    
    def __str__(self):
        res = ""
        for i in self.stack:
            res += str(i) + "->"
        return res[:-2] if len(res) else "empty"
    
stack = Stack()
pattern = "()(())()(())"
flag = True
for i in pattern:
    if i == '(':
        stack.push(i)
    elif stack.isEmpty():
        flag = False
        break
    else:
        stack.pop()

print("Final pattern is complete: ", stack.isEmpty() and flag)