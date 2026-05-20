from collections import deque
class BSTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert_node(node_val, root_node):
    if not root_node:
        return "No binary tree"
    elif node_val <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BSTree(node_val)
        else:
            insert_node(node_val, root_node.left_child)
    else:
        if root_node.right_child is None:
            root_node.right_child = BSTree(node_val)
        else:
            insert_node(node_val, root_node.right_child)
    return "Node successfully inserted"

def level_order_traversal(root_node):
    if not root_node:
        return "No tree"
    queue = deque([root_node])
    
    while queue:
        current = queue.popleft()
        print(current.data)
        
        if current.left_child:
            queue.append(current.left_child)
        if current.right_child:
            queue.append(current.right_child)
            
my_tree = BSTree(50)
insert_node(40, my_tree)
insert_node(34, my_tree)
insert_node(67, my_tree)
insert_node(45, my_tree)
insert_node(89, my_tree)
insert_node(22, my_tree)


level_order_traversal(my_tree)