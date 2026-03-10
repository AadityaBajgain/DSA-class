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
        
    def insert(self, index, val):
        new_node = Node(val)
        temp = self.head
        if index < 0 or index > self.length:
            return None
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        else: 
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1   
        
        
        
        
cir_linked_list = CircularLinkedList()
cir_linked_list.append(50)
cir_linked_list.append(40)

# print(cir_linked_list.head.value)
# print(cir_linked_list.head.next.value)
# print(cir_linked_list.tail.value)
# print(cir_linked_list.tail.next.value)
# print(cir_linked_list)

cir_linked_list.prepend(30)
cir_linked_list.prepend(20)

cir_linked_list.insert(0,10)
cir_linked_list.insert(cir_linked_list.length, 60)
print(cir_linked_list)
