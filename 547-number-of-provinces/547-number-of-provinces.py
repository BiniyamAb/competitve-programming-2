class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                    rank[rootX] += rank[rootY]
                else:
                    root[rootX] = rootY
                    rank[rootY] += rank[rootX]
        
        for x in range(n):
            for y in range(len(isConnected[0])):
                if x!=y and (isConnected[x][y] == 1 or find(x) == find(y)): union(x, y)
        
        return len(set(root))