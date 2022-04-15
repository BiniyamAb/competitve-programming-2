class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree, sources, safes = {}, {}, []
        for i in range(len(graph)): sources[i], outdegree[i] = [], 0
        for i in range(len(graph)):
            for dst in graph[i]:
                outdegree[i] += 1
                sources[dst].append(i)
        
        queue = deque()
        for i in range(len(graph)):
            if outdegree[i] == 0: queue.append(i)

        while queue:
            curr = queue.popleft()
            for node in sources[curr]:
                outdegree[node]-=1
                if outdegree[node] == 0: queue.append(node)
            safes.append(curr)
            
        safes.sort()
        return safes
            
        
                
        