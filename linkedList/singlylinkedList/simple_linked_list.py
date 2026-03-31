class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class SinglyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        
        self.head = new_node
        self.tail = new_node
        
        self.length = 1
        

new_linked_list = SinglyLinkedList(10)
print(new_linked_list.head.value)
print(new_linked_list.length)