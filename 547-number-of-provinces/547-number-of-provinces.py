class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootY] > rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootX] = rootY
                    rank[rootY] += 1
        
        for x in range(n):
            for y in range(len(isConnected[0])):
                if x!=y and (isConnected[x][y] == 1 or find(x) == find(y)): union(x, y)
        
        return len(set(root))