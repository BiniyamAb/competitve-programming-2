class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp = []
        ans = []
        n = 0
        for word in words:
            while n + len(word) + len(temp) >  maxWidth:
                gaps = (len(temp) - 1) or 1
                q, r = divmod(maxWidth - n, gaps)
                for i in range(gaps):
                    temp[i] += (" " * q) + (" " if i < r else "")
                ans.append("".join(temp))
                temp = []
                n = 0
            n += len(word)
            temp.append(word)
            
        if temp:
            temp = " ".join(temp)
            temp += (" " * (maxWidth - len(temp)))
            ans.append(temp)
            
        return ans
        