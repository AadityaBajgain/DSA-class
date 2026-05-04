#  imagine a stack of plates. If the stack gets too high, it might topple.Therefore, in real life, you would like to start a new stack with the previous stack exceeds some threshold.

# Implement a data structure set of stacks that mimics this. Set of stacks, should be composed of several

# stacks and should create a new stack once the previous one exceeds the capacity.

# Push and pop methods should behave identically to a single stack.

# That is, pop should return the same value as it would if there were just a single stack.

# Then we have a follow up here in this question.

# We need to implement popAt function, which performs a pop operation on a specific sub-stack



class SetOfPlates:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity
        
    
    def push(self, val):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
            
        
        self.stacks[-1].append(val)
        
    
    def pop(self):
        if not self.stacks:
            raise Exception("Stack is empty")
        
        value = self.stacks[-1].pop()
        
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return value
    

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            raise Exception("Index out of bound")
        
        value = self.stacks[index].pop()
        
        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)
        
        return value
    

stack = SetOfPlates(3)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.stacks)

stack.popAt(1)

print(stack.stacks)