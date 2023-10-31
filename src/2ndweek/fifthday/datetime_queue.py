from datetime import datetime

class Queue:
    def __init__(self) -> None:
        self.items = []

    def enqueue(self,items):
        self.items.append(items)

    def is_empty(self):
        if not self.items:
            return True
        return False
    
    def dequeue(self,number_of_items=1):
        counter = 0
        while not self.is_empty() and counter< number_of_items:
            self.items.pop(0)
            counter = counter + 1
    
    def __str__(self) -> str:
        res = "start - \n"
        for item in self.items:
            res += str(item) + "\n "
        return res + '-end'

q = Queue()
q.enqueue(datetime.now())
q.enqueue(datetime(2023, 1, 15, 12, 0))
q.enqueue(datetime(2013, 2, 25, 22, 0))
q.enqueue(datetime(2003, 3, 2, 12, 0))

print(q)
