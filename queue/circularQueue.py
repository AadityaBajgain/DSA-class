class CircularQueue:
    def __init__(self, max_size):
        self.items = [None]*max_size
        self.max_size = max_size
        self.start = -1
        self.top = -1
        
    
    def __str__(self):
        value = [str(x) for x in self.items]
        return " ".join(value)
    

    def is_full(self):
        if self.start == self.top + 1:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False
        
    def is_empty(self):
        if self.start == -1:
            return True
        else:
            return False
        
    
    def enqueue(self, val):
        if self.is_full():
            return "queue is full"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = val
            return "value added in the queue"
        
    def dequeue(self):
        if self.is_empty():
            return "There is no items in the queue"
        else:
            first_item = self.items[self.start]
            start = self.start
            
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_item
    
    def peek(self):
        if self.is_empty():
            return "This queue is empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.max_size * [None]
        
        self.start = -1
        self.top = -1
        

my_queue = CircularQueue(5)

my_queue.enqueue(10)
my_queue.enqueue(10)
my_queue.enqueue(10)
my_queue.enqueue(10)
my_queue.enqueue(10)
my_queue.enqueue(15)
print(my_queue.start)
print(my_queue.top)
    
print(my_queue.is_full())
print(my_queue)


my_queue.dequeue()
my_queue.dequeue()

print(my_queue)

print(my_queue.peek())


my_queue.delete()

print(my_queue)