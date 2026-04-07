class stack:
    def __init__(self):
        self.items = []
        self.length = 0
        
        
    def push(self, val):
        self.items.append(val)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        if self.is_empty:
            return "stack is empty"
        values = [str(value) for value in reversed(self.items)]
        return "\n".join(values)
    
    def is_empty(self):
        return len(self.items) == 0
    
my_stack = stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)

print(my_stack.items)
print(len(my_stack))
print(my_stack)