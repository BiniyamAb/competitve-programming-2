class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_prerequisite = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for a, b in prerequisites:
            is_prerequisite[a][b] = True
        
        # for i in range(numCourses): is_prerequisite[i][i] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    is_prerequisite[i][j] = is_prerequisite[i][j] or (is_prerequisite[i][k] and is_prerequisite[k][j])
        
        for i in range(len(queries)):
            u, v = queries[i]
            queries[i] = is_prerequisite[u][v]
        
        return queries