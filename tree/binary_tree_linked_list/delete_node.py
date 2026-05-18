from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
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
            
def get_deepest_node(root):
    if not root:
        return
    else:
        queue = deque([root])
        
        while queue:
            current = queue.popleft()

            if current.left_child:
                queue.append(current.left_child)
            if current.right_child:
                queue.append(current.right_child)
        
        return current
    
def delete_deepest_node(root, dnode):
    if not root:
        return
    else:
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            if current.left_child:
                if current.left_child is dnode:
                    current.left_child = None
                    return
                else:
                    queue.append(current.left_child)
            if current.right_child:
                if current.right_child is dnode:
                    current.right_child = None
                    return
                else:
                    queue.append(current.right_child)


def delete_node(root_node, target_node):
    if not root_node:
        return
    else:
        queue = deque([root_node])
        
        while queue:
            current = queue.popleft()
            
            if current is target_node:
                dnode = get_deepest_node(root_node)
                current.data = dnode.data
                delete_deepest_node(root_node, dnode)
            else:
                if current.left_child:
                    queue.append(current.left_child)
                if current.right_child:
                    queue.append(current.right_child)

                
                
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


# dnode = get_deepest_node(new_bt)
# delete_deepest_node(new_bt, dnode)


delete_node(new_bt, cold)
level_order_traversal(new_bt)