from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
def search_node(root, target):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.data == target:
            return current
        else:
            if current.left_child:
                queue.append(current.left_child)
            if current.right_child:
                queue.append(current.right_child)
                
def level_order_traversal(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        print(current.data)
        
        if current.left_child:
            queue.append(current.left_child)
        if current.right_child:
            queue.append(current.right_child)
        
def add_node(root, new_node):
    if not root:
        root = new_node
    else:
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            
            if current.left_child:
                queue.append(current.left_child)
            else:
                current.left_child = new_node
                return
            if current.right_child:
                queue.append((current.right_child))
            else:
                current.right_child = new_node
                return


new_bt = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")

new_bt.left_child = hot
new_bt.right_child = cold

cola = TreeNode("cola")
fanta = TreeNode("fanta")

cold.left_child = cola
cold.right_child = fanta

coffee = TreeNode("Coffee")
tea = TreeNode("Tea")

hot.left_child = coffee
hot.right_child = tea


print(search_node(new_bt,"cola").data)

add_node(new_bt, TreeNode("soup"))
level_order_traversal(new_bt)