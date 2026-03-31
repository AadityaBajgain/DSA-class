class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def insert(self, val, index):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            i = 0
            temp = self.head
            while i<index-1:
                temp = temp.next
                i+=1
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        
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
    
    def search(self,val):
        temp = self.head
        i = 0
        if self.head is None:
            return None
        else:
            while temp:
                if temp.value == val:
                    return i
                temp = temp.next
                i += 1
    def get(self, index):
        if index == -1:
            return self.tail
        
        if index < -1 or index > self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            if temp.next:
                temp = temp.next
        return temp
    
    def set(self, val, index):
        temp = self.get(index)

        if temp:
            temp.value = val
            return True
        return False
    
    def pop_first(self) -> Node:
        if self.head:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp
    def remove(self, index):
        if index >= self.length:
            return None
        if index < self.length:
            return None
        temp = self.head

        if temp:
            for _ in range(index-1):
                temp = temp.next
            rem_node = temp.next
            temp.next = rem_node.next
            if rem_node == self.tail:
                self.tail = temp
            rem_node.next = None
                
        return rem_node
        
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(30)
new_linked_list.append_front(5)
new_linked_list.append_front(2)
new_linked_list.insert(15, 2)
print(new_linked_list.length)
print(new_linked_list.head.value)
new_linked_list
print(new_linked_list)
print(new_linked_list.search(15))
# print(new_linked_list.get(4))
# print(new_linked_list.set(22, 3))
# print(new_linked_list)
# print(new_linked_list.pop_first().value)
# print(new_linked_list)
print(new_linked_list.remove(new_linked_list.length))
print(new_linked_list)
print(new_linked_list.tail.value)