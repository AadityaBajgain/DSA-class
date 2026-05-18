class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size
        
    def insert_node(self, val):
        if self.last_used_index+1 == self.max_size:
            return "Binary tree is full"
        self.custom_list[self.last_used_index+1] = val
        self.last_used_index += 1
        return "Successfully inserted"
    
new_bt = BinaryTree(5) 
new_bt.insert_node("Drinks")
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")

