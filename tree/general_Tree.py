class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level = 0):
        result = " " * level + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level+1)
        return result
    
    def add_child(self,TreeNode):
        self.children.append(TreeNode)
        


tree = TreeNode("drinks",[])
cold = TreeNode("Cold",[])
hot = TreeNode("Hot",[])

cola = TreeNode("Cola",[])
fanta = TreeNode("Fanta",[])


coffee = TreeNode("Coffee",[])
tea = TreeNode("Tea",[])

tree.add_child(cold)
tree.add_child(hot)
cold.add_child(cola)
cold.add_child(fanta)
hot.add_child(coffee)
hot.add_child(tea)

print(tree)