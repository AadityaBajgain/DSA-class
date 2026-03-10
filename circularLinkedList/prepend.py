class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp = self.head
        result =""
        
        while temp:
            result += str(temp.value)
            result += " -> "
            temp = temp.next
            if temp == self.head:
                break
        return result
    
    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1
        
        
cir_linked_list = CircularLinkedList()
cir_linked_list.append(10)
cir_linked_list.append(20)

print(cir_linked_list.head.value)
print(cir_linked_list.head.next.value)
print(cir_linked_list.tail.value)
print(cir_linked_list.tail.next.value)
print(cir_linked_list)

cir_linked_list.prepend(5)
cir_linked_list.prepend(1)
print(cir_linked_list)
