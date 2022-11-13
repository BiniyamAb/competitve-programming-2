class Solution:
    def reverseWords(self, s: str) -> str:
        is_word = False
        current_word = []
        res = []
        for literal in s:
            is_letter = literal != " "
            if is_word and is_letter:
                current_word.append(literal)
            elif is_word and not is_letter:
                is_word = False
                word = "".join(current_word)
                res.append(word)
                res.append(" ")
                current_word = []
            elif not is_word and is_letter:
                current_word.append(literal)
                is_word = True
        
        if current_word:
            word = "".join(current_word)
            res.append(word)
        elif res:
            res.pop()
        
        res.reverse()
        return "".join(res)
        
                