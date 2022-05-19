class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = []
        for _ in range(n): answer.append(set())
        indegree, neighbours = defaultdict(int), defaultdict(list)
        
        for i in range(len(edges)):
            fromi, toi = edges[i]
            neighbours[fromi].append(toi)
            indegree[toi]+=1
        
        queue = deque()
        for k in range(n): 
            if indegree[k] == 0: queue.append(k)
                
        while queue:
            curr = queue.popleft()
            for node in neighbours[curr]:
                indegree[node]-=1
                if indegree[node] == 0: queue.append(node)
                answer[node].add(curr)
                for n in answer[curr]: answer[node].add(n) 
        
        for i in range(len(answer)): 
            answer[i] = list(answer[i])
            answer[i].sort()
        
        return answer
                
        
        
        