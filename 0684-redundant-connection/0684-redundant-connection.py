class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        size = [1] * len(edges)
        
        for node1, node2 in edges:
            node1 -= 1
            node2 -= 1
            if self.union(size, parent, node1, node2):
                return [node1+1, node2+1]
                
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent,parent[x])
        
        return parent[x]
    
    def union(self, size, parent, node1, node2):
        node1_parent = self.find(parent,node1)
        node2_parent = self.find(parent,node2)
        
        if node1_parent == node2_parent: return True
        
        if size[node1_parent] >= size[node2_parent]:
            parent[node2_parent] = node1_parent
            size[node1_parent] += size[node2_parent]
        else:
            parent[node1_parent] = node2_parent
            size[node2_parent] += size[node1_parent]
        
        return False
        
        