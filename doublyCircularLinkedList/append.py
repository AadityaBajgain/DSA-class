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
            self.next = self.head
        self.length += 1

dcl = DoublyCircularLinkedList()
dcl.append(10)
dcl.append(20)
dcl.append(30)
dcl.append(40)
dcl.append(50)
print(dcl)