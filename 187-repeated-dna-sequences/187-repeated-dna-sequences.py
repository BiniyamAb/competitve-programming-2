class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:        
        if len(s) <= 10: return [] 
        uniques, repeated, repeatedSet = set(), [], set()
        que = deque([None,s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8]])
        
        for i in range(9,len(s)):
            que.popleft()
            que.append(s[i])
            temp = ""
            for j in range(10):
                temp+=str(ord(que[j]))
                
            temp = int(temp)
            if temp not in uniques:
                uniques.add(temp)
            elif temp not in repeatedSet:
                repeatedSet.add(temp)
                temp = str(temp)
                sequence = ""
                for i in range(0, len(temp), 2):
                    char = temp[i] + temp[i+1]
                    sequence += chr(int(char))
                repeated.append(sequence)
        
        return repeated
        
            
        
        
        