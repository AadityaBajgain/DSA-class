# left subtree --> right subtree --> root node

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

        
        
def post_order_traversal(root):
    if not root:
        return
    post_order_traversal(root.left_child)
    post_order_traversal(root.right_child)
    print(root.data)
    
    

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

post_order_traversal(new_bt)
