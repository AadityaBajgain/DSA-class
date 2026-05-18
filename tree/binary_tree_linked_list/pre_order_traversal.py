class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

        

new_bt = TreeNode("Drinks")
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")

new_bt.left_child = left_child
new_bt.right_child = right_child

def pre_order_traversal(root):
    if not root:
        return
    print(root.data)
    pre_order_traversal(root.left_child)
    pre_order_traversal(root.right_child)
    
    
pre_order_traversal(new_bt)