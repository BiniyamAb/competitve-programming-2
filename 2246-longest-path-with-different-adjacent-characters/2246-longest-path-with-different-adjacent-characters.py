class Solution:
    def dfs(self,i,tree,s):
        max_from_all = 0
        current_max_length = 0
        longest_two = []
        
        for child in tree[i]:
            max_length, length = self.dfs(child,tree,s)
            
            
            if s[i] != s[child]:
                longest_two.append(length)
                current_max_length = max(current_max_length, length)
                if len(longest_two) > 2:
                    longest_two.sort(reverse=True)
                    longest_two.pop()
                
            max_from_all = max(max_from_all, max_length)
            
        
        max_from_all = max(max_from_all, sum(longest_two)+1) 
        
        return [max_from_all, current_max_length+1]
    
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(set)
        for i in range(1,len(parent)):
            tree[parent[i]].add(i)
        
        result = self.dfs(0,tree,s)
        return max(result)
            
            