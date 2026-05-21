from collections import deque

class AVL_tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.height = None
    

def in_order_traversal(root):
    if not root:
        return
    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)

def pre_order_traversal(root):
    if not root:
        return
    print(root.data)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)
    
def post_order_traversal(root):
    if not root:
        return
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.data)
    
def level_order_traversal(root):
    if not root:
        return
    queue = deque(([root]))
    
    while queue:
        current = queue.popleft()
        print(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

            
def search_node(root, node_val):
    if not root:
        return "No Tree to search"
    if root.data == node_val:
        return True
    elif root.data > node_val:
        return search_node(root.left, node_val)
    else:
        return search_node(root.right, node_val)