class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set()
        res = []
        for _, node2 in edges:
            nodes.add(node2)

        for node in range(n):
            if node not in nodes:
                res.append(node)

        return res