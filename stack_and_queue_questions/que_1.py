# use single python list to implement 3 stacks

# class MultiStack:
#     def __init__(self, num_stack, stack_size):
#         self.num_stacks = num_stack
#         self.stack_size = stack_size
#         self.array = [None]* (stack_size * num_stack)
#         self.tops = [-1] * num_stack
        
#     def push(self, stack_num, value):
#         if self.tops[stack_num] == self.stack_size - 1:
#             raise Exception("Stack Overflow")
#         self.tops[stack_num] += 1
#         index = stack_num * self.stack_size + self.tops[stack_num]
#         self.array[index] = value
    
    
#     def pop(self, stack_num):
#         if self.tops[stack_num] == -1:
#             raise Exception("Stack Underflow")
        
#         index = stack_num * self.stack_size + self.tops[stack_num]
#         value = self.array[index]
#         self.array[index] = None
#         self.tops[stack_num] -= 1
#         return value
        

class KStack:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.arr = [0]*n
        self.top = [-1]*k
        self.free = 0
        self.next = list(range(1,n)) + [-1]
        
    def push(self, sn, item):
        if self.free == -1: 
            raise Exception("Stack Overflow")
        
        i = self.free
        
        self.free = self.next[i]
        self.arr[i] = item
        self.next[i] = self.top[sn]
        self.top[sn] = i
    
    def pop(self, sn):
        if self.free == -1:
            raise Exception("Stack Underflow")

        i = self.top[sn]
        
        self.top[sn] = self.next[i]
        self.next[i] = self.free
        self.free = i
        
        

my_stack = KStack(3,10)

my_stack.push(1,11)

my_stack.push(2,22)
my_stack.push(2,23)

print(my_stack.arr)

my_stack.pop(2)

print(my_stack.arr)
my_stack.push(1,12)
print(my_stack.arr)