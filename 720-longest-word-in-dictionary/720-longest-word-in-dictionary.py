class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for ch in word:
            ind = ord(ch) - 97
            if curr.children[ind] == None: curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.end = True
    
    def search(self,word):
        curr = self.root
        for ch in word:
            ind = ord(ch) - 97
            if curr.children[ind] == None: return False
            curr = curr.children[ind]
        
        return curr.end
    
    def prefix(self,pre):
        curr = self.root
        for ch in pre:
            ind = ord(ch) - 97
            if curr.children[ind] == None: return False
            curr = curr.children[ind]
            
        return True
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        word_trie = Trie()
        longest = ""
        for word in words: 
            if len(word) == 1 or word_trie.prefix(word[:-1]):
                word_trie.insert(word)
                if len(word) > len(longest):
                    longest = word
        
        return longest
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        