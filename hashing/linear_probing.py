class LinearProbing:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
    
    def hash_function(self, val):
        return val % self.size
    
    def insert(self, val):
        index = self.hash_function(val)
        
        i = 0
        
        while i < self.size:
            
            current = (index + i) % self.size
            if self.table[current] is None: 
                self.table[current] = val 
                return
            i += 1
        raise Exception("Table Overflow")
    
    def search(self, val):
        index = self.hash_function(val)
        
        i = 0
        
        while i < self.size:
            current = (index + i) % self.size
            
            if self.table[current] == None: return False
            if self.table[current] == val: return True
            
            i += 1
        return False


lp = LinearProbing(10)

lp.insert(10)
lp.insert(11)
lp.insert(12)
lp.insert(13)
lp.insert(14)
lp.insert(15)
lp.insert(16)
lp.insert(17)
lp.insert(18)
lp.insert(19)
print(lp.table)
# lp.insert(20)
print(lp.table)

print(lp.search(20))
print(lp.search(11))