class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for ch in word:
            ind = ord(ch) - ord("a")
            if curr.children[ind] == None: curr.children[ind] = TrieNode()
            curr.children[ind].count+=1
            curr = curr.children[ind]
    
    def prefixCount(self,pre):
        curr = self.root
        for ch in pre:
            ind = ord(ch) - ord("a")
            if curr.children[ind] == None: return 0
            curr = curr.children[ind]
        
        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        words_trie = Trie()
        for word in words: words_trie.insert(word)
        return words_trie.prefixCount(pref)