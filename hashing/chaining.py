class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
        
    def hash_function(self, keys):
        return keys % self.size
    
    def sortInsert(self, val):
        index = self.hash_function(val)
        
        if self.table[index] == None:
            self.table[index] = Node(val)
            return

        new_node = Node(val)
        if self.table[index].val > val:
            new_node.next = self.table[index]
            self.table[index] = new_node
            return

        current = self.table[index]
        
        while current.next and current.next.val < val:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        
    def search(self, val):
        index = self.hash_function(val)
        if self.table[index] == None:
            return False
        if self.table[index].val > val:
            return False
        
        temp = self.table[index]
        
        while temp:
            if temp.val == val:
                return True
            temp = temp.next

    def delete(self,val):
        
        index = self.hash_function(val)
        
        temp = self.table[index]
        if temp == None:
            return None
        if temp.val == val:
            self.table[index] = temp.next
            temp.next = None
            return temp
        while temp.next:
            nxt = temp.next
            if nxt.val == val:
                temp.next = nxt.next
                nxt.next = None
                return nxt
            if nxt.val < val:
                temp = temp.next
            else:
                return None
        return None
        
hashh = HashTable(10)

hashh.sortInsert(20)
hashh.sortInsert(3)
hashh.sortInsert(55)
hashh.sortInsert(23)
hashh.sortInsert(12)


print(hashh.search(45))

print(hashh.delete(20).val)

print(hashh.search(20))
print(hashh.search(12).val)