from random import randint

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        values = [str(x.value) for x in self]
        return " -> ".join(values)
    
    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next
    
    def __len__(self):
        count = 0
        curr_node = self.head
        
        while curr_node:
            count += 1
            
            curr_node = curr_node.next
            
        return count
    
    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        return self.tail
    
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        
        for _ in range(n):
            self.add(randint(min_value, max_value))
            
        return self
    
    


if __name__ == "__main__":
    ll = LinkedList()
    ll.generate(10, 20, 100)
    print(ll)
    print(len(ll))