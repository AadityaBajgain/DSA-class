class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
        self.length = 0
        
    def append(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
        
    def append_front(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            temp = new_node
            temp.next = self.head
            
            self.head = new_node
        self.length += 1
        
    def __str__(self):
        
        temp = self.head
        result = ""
        
        while temp:
            result += str(temp.value)
            if temp.next is not None:
                result += " -> "
            temp = temp.next
        return result
    
    
    
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(30)
new_linked_list.append_front(5)
new_linked_list.append_front(2)

print(new_linked_list.length)
print(new_linked_list.head.value)

print(new_linked_list)