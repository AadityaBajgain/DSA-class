class Queue:
    
    
    def __init__(self):
        self.items = []
        self.length = 0
        
    def __str__(self):
        values = [str(value) for value in self.items]
        return " ".join(values)
    
    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, val):
        self.items.append(val)
        self.length += 1
    
    def dequeue(self):
        if self.is_empty():
            return "No items in the queue."
        self.length -= 1
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "No items in the queue."
        return self.items[0]

    def delete(self):
        self.items = []
    
    
    
    
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)


print(my_queue)


my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

print(my_queue)

print(my_queue.peek())