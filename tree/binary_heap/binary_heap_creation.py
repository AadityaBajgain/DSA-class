class BinaryHeap:
    def __init__(self, size):
        self.list = [None] * (size+1)
        self.heap_size = 0
        self.max_size = size+1
        
    def size(self):
        if not self.list:
            return
        return self.heap_size
    
    def level_order_traversal(self):
        if not self.list:
            return
        for i in range(1, self.heap_size +1):
            print(self.list[i])
            
    def peek(self):
        if not self.list:
            return
        return self.list[1]
    
    # def heapifyInsert(self, index, heap_type):
    #     parent = int(index/2)
    #     if index <= 1:
    #         return
    #     if heap_type == "min":
    #         if self.list[index] < self.list[parent]:
    #             self.list[index],self.list[parent] = self.list[parent],self.list[index]
            
    #         self.heapifyInsert(parent,heap_type)
        
    #     if heap_type == "max":
    #         if self.list[index] > self.list[parent]:
    #             self.list[index],self.list[parent] = self.list[parent],self.list[index]
            
    #         self.heapifyInsert(parent,heap_type)
    
    def heapifyInsert(self, index, heap_type):
        while index > 1:
            parent = index // 2
            
            if (
                (heap_type == "min" and self.list[index] < self.list[parent])
                or 
                (heap_type == "max" and self.list[index] > self.list[parent])
            ):
                self.list[index], self.list[parent] = self.list[parent], self.list[index]
                index = parent
            else:
                break
        
    def insert_node(self, node_val, heap_type):
        if self.heap_size + 1 == self.max_size:
            return "heap is full"
        self.list[self.heap_size + 1] = node_val
        self.heap_size += 1
        self.heapifyInsert(self.heap_size, heap_type)
        return "successfully inserted"
    
    
    def delete_node(self, heap_type):
        if self.heap_size == 0:
            return "heap is empty"
        deleted_node = self.list[1]
        self.list[1] = self.list[self.heap_size]
        self.list[self.heap_size] = None
        self.heap_size -= 1
        
        i = 1
        
        while True:
            left = i * 2
            right = i * 2 + 1
            swap_child = i
            
            if heap_type == "min":
                if left <= self.heap_size and self.list[left] < self.list[swap_child]:
                    swap_child = left
                if right <= self.heap_size and self.list[right] < self.list[swap_child]:
                    swap_child = right
                    
            elif heap_type == "max":
                if left <= self.heap_size and self.list[left] > self.list[swap_child]:
                    swap_child = left
                if right <= self.heap_size and self.list[right] > self.list[swap_child]:
                    swap_child = right 
            
            if swap_child == i:
                break
            
            self.list[swap_child], self.list[i] = self.list[i], self.list[swap_child]
            i = swap_child
        
        return deleted_node
    
    
    def delete_bh(self):
        self.list = None

my_bh = BinaryHeap(10)

my_bh.insert_node(5, "min")
my_bh.insert_node(10, "min")
my_bh.insert_node(20, "min")
my_bh.insert_node(30, "min")
my_bh.insert_node(40, "min")
my_bh.insert_node(50, "min")
my_bh.insert_node(60, "min")

my_bh.level_order_traversal()

print("___" * 30)


my_bh.delete_node("min")

my_bh.level_order_traversal()


def heapify(root, index, type):
    if index <= 1:
        return
    parent= int(index/2)
    
    