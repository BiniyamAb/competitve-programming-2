class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        max_sum = max(vals)
        if len(edges) == 0: return max_sum
        graph = defaultdict(list)
        for u, v in edges:
            if vals[v] > 0:
                heappush(graph[u], vals[v])
                
            if vals[u] > 0:
                heappush(graph[v], vals[u])
            
            if len(graph[u]) > k:
                heappop(graph[u])
            
            if len(graph[v]) > k:
                heappop(graph[v])
        
        for key, val in graph.items():
            curr_sum = vals[key] + sum(val)
            max_sum = max(curr_sum, max_sum)
        
        return max_sum