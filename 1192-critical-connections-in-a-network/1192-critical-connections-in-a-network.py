class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(v, parent, current_time):
            times[v] = current_time
            for nei in adj_list[v]:
                if nei == parent:
                    continue
                elif times[nei] == None:
                    dfs(nei, v, current_time + 1)
                
                if times[nei] > current_time:
                    critial_connections.append((nei, v))
                times[v] = min(times[v], times[nei])

        adj_list = defaultdict(list)
        for u,v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
                
        critial_connections = []
        times = [None] * n
        
        dfs(0, None, 0)
                
        return critial_connections
        