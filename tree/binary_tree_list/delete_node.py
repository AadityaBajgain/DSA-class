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

    def pre_order_traversal(self, index = 1):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)
    
    def in_order_traversal(self, index = 1):
        if index > self.last_used_index:
            return
        self.in_order_traversal(index * 2)
        print(self.custom_list[index])
        self.in_order_traversal(index * 2 + 1)

    def post_order_traversal(self, index = 1):
        if index > self.last_used_index:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.custom_list[index])
        
    def level_order_traversal(self):
        # if self.custom_list is None:
        #     return
        for i in range(1,self.last_used_index + 1):
            print(self.custom_list[i])
    
    def delete_node(self, node_val):
        if not self.custom_list:
            return "No binary tree"
        temp_node = self.custom_list[self.last_used_index]
        for i in range(1,self.last_used_index+1):
            if self.custom_list[i] == node_val:
                self.custom_list[i] = temp_node
                self.custom_list.pop()
                self.last_used_index -= 1
                return temp_node
        
new_bt = BinaryTree(5) 
new_bt.insert_node("Drinks")
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")
# print(new_bt.node_search("Hot"))

# new_bt.pre_order_traversal()

# new_bt.in_order_traversal()
# new_bt.post_order_traversal()


new_bt.delete_node("Cold")
new_bt.level_order_traversal()