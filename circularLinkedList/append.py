class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        

cir_linked_list = CircularLinkedList()
cir_linked_list.append(10)
cir_linked_list.append(20)
