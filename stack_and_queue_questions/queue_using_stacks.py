# implement queue using 2 stacks

class QueueWithStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    
    def enqueue(self, value):
        self.in_stack.append(value)
    
    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                
        if not self.out_stack:
            raise Exception("Queue is empty")
        
        return self.out_stack.pop()
    


stack = QueueWithStacks()

stack.enqueue(10)
stack.enqueue(11)
stack.enqueue(12)
stack.enqueue(13)
stack.enqueue(14)

print(stack.in_stack)
print(stack.out_stack)



stack.dequeue()
stack.dequeue()
stack.dequeue()


print(stack.in_stack)
print(stack.out_stack)