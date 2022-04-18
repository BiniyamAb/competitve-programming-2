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
            rootX, rootY = sorted([rootX, rootY], key=lambda i: rank[i])
            if rootX != rootY:
                root[rootX] = rootY
                rank[rootY] += rank[rootX]
                rank[rootX] -= rank[rootX]
        
        def connected(x,y):
            return find(x) == find(y)
        
        for x in range(n):
            for y in range(len(isConnected[0])):
                if x!=y and (isConnected[x][y] == 1 or connected(x,y)): union(x, y)
        
        count = 0
        for ele in rank: count += 1 if ele != 0 else 0
        return count