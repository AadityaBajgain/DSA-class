class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    
    def __iter__(self):
        temp = self.head
        
        while temp:
            yield temp
            temp = temp.next
            
        
class Queue:
    def __init__(self):
        self.linked_list = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return " ".join(values)
    
    def enqueue(self, val):
        new_node = Node(val)
        
        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node
            
        self.linked_list.length += 1
                
                
    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        temp = self.linked_list.head
        if self.linked_list.head == self.linked_list.tail:
            self.linked_list.head = self.linked_list.tail = None
        else: 
            self.linked_list.head = temp.next
            temp.next = None
        self.linked_list.length -= 1
        return temp
    def peek(self):
        return self.linked_list.head
    
    def is_empty(self):
        return self.linked_list.head == None
    
    
    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None
        self.linked_list.length = 0
    
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(11)
my_queue.enqueue(12)
my_queue.enqueue(13)
my_queue.enqueue(14)

print(my_queue)
print(my_queue.linked_list.length)

my_queue.dequeue()
print(my_queue)
# print(my_queue.linked_list.tail.value)

print(my_queue.linked_list.length)

my_queue.delete()
print(my_queue)