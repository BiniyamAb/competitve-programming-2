class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.children: curr.children[ch] = TrieNode()
            curr.children[ch].count+=1
            curr = curr.children[ch]
    
    def prefixCount(self,pre):
        curr = self.root
        for ch in pre:
            if ch not in curr.children: return 0
            curr = curr.children[ch]
        
        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        words_trie = Trie()
        for word in words: words_trie.insert(word)
        return words_trie.prefixCount(pref)