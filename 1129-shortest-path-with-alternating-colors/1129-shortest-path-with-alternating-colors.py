class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        answer = [float("inf")] * n
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        for a, b in redEdges: red_graph[a].append(b)
        for u, v in blueEdges: blue_graph[u].append(v)
        graphs = [red_graph,blue_graph]
        
        def bfs(dest, graphs):
            visited = [set(), set()]
            queue = deque([(0,0),(0,1)])
            level = 0
            
            while queue:
                n = len(queue)
                for _ in range(n):
                    current_node, color_index = queue.popleft()
                    color_index = 1 - color_index
                    # answer[current_node] = level
                    if current_node == dest: return level
                    for neighbour in graphs[color_index][current_node]:
                        if neighbour not in visited[color_index]:
                            queue.append((neighbour,color_index))
                            visited[color_index].add(neighbour)
                level += 1
            
            return -1
        
        for i in range(n):
            answer[i] = bfs(i, graphs)            
        
        return answer