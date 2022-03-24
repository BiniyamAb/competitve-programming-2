class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        end, IndStop, res = 0, 0, []
        
        
        for i in range(len(s)):
            while freq[s[i]] > 0 and end < len(s):
                freq[s[end]] -= 1
                end+=1
            
            if i == end-1:
                res.append(end - IndStop)
                IndStop = end
                
        return res
                
            
                    
                    
            