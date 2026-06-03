class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    # def insert(self, word):
    #     current = self.root
    #     for i in word:
    #         node = current.children.get(i)
            
    #         if node == None:
    #             node = TrieNode()
    #             current.children.update({i:node})
    #         current = node
    #     current.end_of_string = True
    
    def insert(self, word):
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_string = True
    
    def search_string(self, word):
        current = self.root
        
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        
        return current.end_of_string

    def has_prefix(self, prefix):
        current = self.root
        
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True

    def delete_word(self,word):
        def _delete(current_node,word, index):
            
            # case 1: the node is at the leaf of the tree
            if index == len(word):
                
                # this marks node as the end of the word
                if not current_node.end_of_string:
                    return False
                
                current_node.end_of_string = False
                
                # this will allow the function to delete it, as it does not have any children
                return len(current_node.children) == 0
            
            
            # this will take every character at the given index
            c = word[index]
            
            node = current_node.children.get(c)
            
            # if the node is None, word does not exist, so return False
            if node is None:
                return False
            
    
            delete_current_node = _delete(node, word, index + 1)
            
            
            if delete_current_node:
                del current_node.children[c]
                
                # this makes sure that current node having other children and prefix for other word is not deleted
                return len(current_node.children) == 0 and not current_node.end_of_string
            
            return False
        
        _delete(self.root, word, 0)
        
        
newTrie = Trie()
newTrie.insert("App")
newTrie.insert("Api")
newTrie.insert("Appl")
print(newTrie.search_string("App"))

print(newTrie.search_string("Api"))
newTrie.delete_word("Api")
print(newTrie.search_string("Api"))