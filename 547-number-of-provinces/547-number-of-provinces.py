class Solution:
    def dfs(self, row, isConnected):
        self.visited.add(row)
        for col in range(len(isConnected[row])):
            if row != col and isConnected[row][col] == 1 and col not in self.visited:
                self.dfs(col, isConnected)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        self.visited = set()
        for row in range(len(isConnected)):
            if row not in self.visited:
                self.dfs(row, isConnected)
                provinces+=1
        
        return provinces
        