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
        
        if current.end_of_string == True:
            return True
        else:
            return False
    def delete_string(self,root, word, index = 0):
        ch = word[index]
        current = root.children[ch]
        can_this_node_be_deleted = False
        
        if len(current.children) > 1:
            self.delete_string(current,word, index+1)
            return False
        if index == len(word) - 1:
            if len(current.children) >= 1:
                current.end_of_string = False
                return False
            else:
                root.children.pop(ch)
                return True
        if current.end_of_string == True:
            self.delete_string(current,word, index+1)
            return False
        
        can_this_node_be_deleted = self.delete_string(current,word,index+1)
        if can_this_node_be_deleted == True:
            root.children.pop(ch)
            return True
        else:
            return False


    
newTrie = Trie()
newTrie.insert("App")
newTrie.insert("Appl")
newTrie.delete_string(newTrie,"App")
print(newTrie.searchString("App"))