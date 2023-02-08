class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in adjacentPairs:
            graph[u].add(v)
            graph[v].add(u)
        
        curr = None
        for k, v in graph.items():
            if len(v) == 1:
                curr = k
                break
        
        res = [curr]
        for _ in range(len(adjacentPairs)):
            temp = curr
            curr = graph[curr].pop()
            graph[curr].remove(temp)
            res.append(curr)
        
        return res
            
        