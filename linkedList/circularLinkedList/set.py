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
        
    def search(self, val):
        if not self.head:
            return None
        
        temp = self.head
        
        i = 0
        while temp:
            if temp.value == val:
                return i
            else:
                temp = temp.next
                i+=1
            if temp == self.head:
                return None
        
    def get(self, index):
        if index == 0:
            return self.head
        if index == -1 or index == self.length - 1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
        
    def set(self,index, val):
        if index < -1 or index >= self.length:
            return None
        
        temp = self.head
        new_node = Node(val)
        if index == 0:
            new_node.next = temp
            self.head = new_node
        if index == -1:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.tail = new_node

        else:
            for _ in range(index - 1):
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

print(cir_linked_list.search(70))

# cir_linked_list2 = CircularLinkedList()

# print(cir_linked_list2.search(10))

print(cir_linked_list.get(5).value)

cir_linked_list.set(-1, 70)

print(cir_linked_list.length)
print(cir_linked_list)