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
def pre_order_traversal(root):
    if not root:
        return
    print(root.data)
    pre_order_traversal(root.left_child)
    pre_order_traversal(root.right_child)
    
def delete_node(root, key):
    if root is None:
        return root
    elif root.data > key:
        root.left_child = delete_node(root.left_child, key)
    elif root.data < key:
        root.right_child = delete_node(root.right_child, key)
    else:
        if root.left_child is None:
            return root.right_child
        if root.right_child is None:
            return root.left_child
        
        curr = root.right_child
        while curr.left_child:
            curr = curr.left_child
        root.data = curr.data
        root.right_child = delete_node(root.right_child, curr.data)
    return root

def delete_tree(root):
    if root:
        root = None
        root.left_child = None
        root.right_child = None
my_tree = BSTree(50)
insert_node(40, my_tree)
insert_node(34, my_tree)
insert_node(67, my_tree)
insert_node(45, my_tree)
insert_node(89, my_tree)
insert_node(10, my_tree)
insert_node(100, my_tree)
insert_node(55, my_tree)


# level_order_traversal(my_tree)

pre_order_traversal(my_tree)

delete_node(my_tree, 55)

print("\t")

pre_order_traversal(my_tree)