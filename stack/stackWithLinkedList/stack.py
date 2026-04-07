class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        

class Stack:
    
    def __init__(self):
        self.top = None
        self.length = 0
        
    def __str__(self):
        temp = self.top
        
        if temp == None:
            return "Stack is empty"
        result = ""
        
        while temp:
            result += str(temp.value)
            if temp.next:
                result += " -> "
            temp = temp.next
        
        return result
    
    def push(self, val):
        new_node = Node(val)
        
        if self.top == None:
            self.top = new_node
            return 
        new_node.next = self.top
        self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.top == None:
            return "Stack is empty"
        temp = self.top
        self.top = temp.next
        self.length -= 1
        return temp

    def peek(self):
        return self.top
    
    
    def is_empty(self):
        return self.top == None
    

    def clear(self):
        self.top = None
        self.length = 0
        
        
my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print(my_stack)
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()

print(my_stack)

print(my_stack.peek().value)