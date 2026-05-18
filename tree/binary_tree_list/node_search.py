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
    
    def node_search(self, node_val):
        if self.custom_list is None:
            return "no binary tree"
        for i in range(0, len(self.custom_list)):
            if self.custom_list[i] == node_val:
                return f"Present in position {i}"
        
        return "Not present"

new_bt = BinaryTree(5) 
new_bt.insert_node("Drinks")
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")
print(new_bt.node_search("Hot"))