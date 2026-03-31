class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
    
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value)
            if temp.next == self.head:
                break
            result += " <-> "
            temp = temp.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            new_node.prev = temp
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1


    def prepend(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
            self.head.prev = self.tail
        self.length += 1

    def search(self, target):
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp:
                if temp.value == target:
                    return True
                if temp.next == self.head:
                    break
                temp = temp.next
            return False
    
    def get(self, index):
        if index < -1 or index >= self.length:
            print("Index out of bound")
            return None
        elif index == 0:
            return self.head
        elif index == self.length - 1 or index == -1:
            return self.tail
        else:
            if index < self.length // 2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                return temp
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
                return temp
            
            
    def set(self, index, val):
        if index < -1 or index >= self.length:
            print("Index out of bound")
            return None
        if index == 0:
            self.head.value = val
            return
        if index == self.length - 1 or index == -1:
            self.tail.value = val
            return      
        else:
            if index < self.length // 2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                temp.value = val
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
                temp.value = val
            return
            
    def pop_first(self):
        if self.head is None:
            return -1
        
        temp = self.head
        self.head = temp.next
        temp.next = None
        temp.prev = None
        self.head.prev = self.tail
        self.tail.next = self.head
        self.length -= 1
        return temp
            
            
    def pop(self):
        if self.head is None:
            return -1
        temp = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            temp.prev = None
            temp.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return temp
    
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = popped_node.prev = None
        self.length -= 1
        return popped_node
        
        
    def delete_all(self):    
        self.head = None
        self.tail = None
        self.length = 0
    
if __name__ == "__main__":
    dcl = DoublyCircularLinkedList()
    dcl.append(10)
    dcl.append(20)
    dcl.append(30)
    dcl.append(40)
    dcl.append(50)
    dcl.append(60)
    print(dcl.head.prev.value)
    print(dcl)
    dcl.prepend(5)
    print(dcl.tail.next.value)
    print(dcl.search(50))
    print(dcl)
    x = dcl.get(5)
    print(x.value)
    dcl.set(6,100)
    print(dcl.tail.value)
    print(dcl)
    
    print(dcl.pop_first().value)
    print(dcl)
    print(dcl.length)
    print(dcl.head.value)
    print(dcl.tail.next.value)
    print(dcl.head.prev.value)
    
    print(dcl.pop().value)
    print(dcl)
    print(dcl.length)
    print(dcl.tail.value)
    print(dcl.tail.next.value)
    print(dcl.head.prev.value)
    
    
    print(dcl.remove(0).value)
    print(dcl)
    print(dcl.length)
    print(dcl.get(0).value)
    
    dcl.delete_all()
    print(dcl.length)