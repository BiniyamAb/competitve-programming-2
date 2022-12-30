class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        neighbour = defaultdict(set)
        for i in range(len(graph)):
            for node in graph[i]:
                neighbour[i].add(node)
        
        res = []
        lst = []
        def dfs(node):
            lst.append(node)
            if node == len(graph) - 1:
                res.append(lst.copy())
            else:
                for child in neighbour[node]:
                    dfs(child)
            lst.pop()
        
        dfs(0)
        return res
                