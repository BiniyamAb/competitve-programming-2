# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        
        def match(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    count += 1
            
            return count
        
        word_set = set(words)
        while word_set:
            curr_word = word_set.pop()
            guess_value = master.guess(curr_word)
            if guess_value == 6: return
            curr_list = list(word_set)
            for word in curr_list:
                if match(curr_word, word) != guess_value:
                    word_set.remove(word)
                
                
            
        
        