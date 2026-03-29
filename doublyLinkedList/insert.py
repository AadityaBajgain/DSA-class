class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
        
    def prepend(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    def __str__(self):
        temp = self.head
        result =""
        while temp != None:
            result += str(temp.value)
            if temp.next != None:
                result += " <-> "
            temp = temp.next
        return result
    
    def search(self, val):
        current = self.head
        index = 0
        while current:
            if current.value == val:
                return index
            current = current.next
            index+=1
        return -1
    
    def get(self, index):
        current = self.head
        if index == 0:
            return current
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length // 2:
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1,index,-1):
                current = current.prev
        return current
        
        
    def set(self,index,val):
        set_node = self.get(index)
        if set_node:
            set_node.value = val
            return True
        return False
    
    
    def insert(self,index,val):
        new_node = Node(val)
        
        if index < -1 or index > self.length:
            print("Index out of bound")
            return
        elif index == 0:
            self.prepend(val)
            return
        elif index == self.length or index == -1:
            self.append(val)
            return
        elif index >= self.length // 2:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
        self.length += 1
        
            
        

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.prepend(5)
print(dll)
print(dll.search(30))
print(dll.get(4).value)
dll.set(3,25)
print(dll)
dll.insert(2,15)
print(dll)
dll.insert(0,1)
print(dll)
dll.insert(7,45)
print(dll)
print(dll.length)