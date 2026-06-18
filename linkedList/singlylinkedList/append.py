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
        
    def __str__(self):
        result = ""
        while self.head:
            result += str(self.head.value)
            if self.head.next is not None:
                result+=" -> "
            self.head = self.head.next
        return result

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(30)

print(new_linked_list.length)
print(new_linked_list.head.value)

print(new_linked_list)