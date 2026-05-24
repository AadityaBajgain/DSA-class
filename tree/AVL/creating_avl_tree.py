from collections import deque

class AVL_tree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.height = 1
    

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
    queue = deque([root])
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

def get_height(root):
    if not root:
        return 0
    return root.height

def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)

def rotate_left(root):
    new_node = root.right
    root.right = new_node.left
    new_node.left = root
    
    root.height = 1 + max(get_height(root.left) , get_height(root.right))
    new_node.height = 1 + max(get_height(new_node.left) , get_height(new_node.right))
    
    return new_node

def rotate_right(root):
    new_node = root.left
    root.left = new_node.right
    
    new_node.right = root
    
    root.height = 1 + max(get_height(root.left) , get_height(root.right))
    new_node.height = 1 + max(get_height(new_node.left) , get_height(new_node.right))
    
    return new_node


def insert_node(root, key):
    if not root:
        return AVL_tree(key)
    elif root.data > key:
        root.left = insert_node(root.left, key)
    else:
        root.right = insert_node(root.right, key)
    
    root.height = 1 + max(get_height(root.left),get_height(root.right))
    
    balance = get_balance(root)
    
    if balance > 1 and root.left.data > key:
        return rotate_right(root)
    if balance > 1 and root.left.data < key:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and root.right.data < key:
        return rotate_left(root)
    if balance < -1 and root.right.data > key:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    
    return root



def delete_node(root, key):
    if not root:
        return root
    elif key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        curr = root.right
        while curr.left:
            curr = curr.left
        root.data = curr.data
        
        root.right = delete_node(root.right, curr.data)
        
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    
    if not root:
        return root
    balance = get_balance(root)
    
    if balance > 1 and get_balance(root.left) >= 0:
        return rotate_right(root)
    if balance > 1 and get_balance(root.right) <= 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and get_balance(root.right) > 0:
        return rotate_left(root)
    if balance < -1 and get_balance(root.right)<0:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root
    

def delete_AVL(root):
    root.data = None
    root.left = None
    root.right = None
    

my_avl = AVL_tree(30)
my_avl = insert_node(my_avl,25)
my_avl = insert_node(my_avl,35)
my_avl = insert_node(my_avl,20)
my_avl = insert_node(my_avl,15)
my_avl = insert_node(my_avl,5)
my_avl = insert_node(my_avl,10)
my_avl = insert_node(my_avl,50)
my_avl = insert_node(my_avl,60)
my_avl = insert_node(my_avl,70)
my_avl = insert_node(my_avl,65)



pre_order_traversal(my_avl)

my_avl = delete_node(my_avl, 50)

print("--"*40)

level_order_traversal(my_avl)

delete_AVL(my_avl)
level_order_traversal(my_avl)