class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = set()
        queue = deque([source])
        while queue:
            curr = queue.popleft()
            for neighbour in graph[curr]:
                if neighbour == destination:
                    return True
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        
        return False
        