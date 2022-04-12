class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree, neighbours, courses = {}, {}, 0
        neighbours = {}
        for j in range(numCourses): indegree[j], neighbours[j] = 0, []
        for i in range(len(prerequisites)):
            src, dst = prerequisites[i]
            indegree[dst] += 1
            neighbours[src].append(dst)
            
        queue = deque()
        for k, v in indegree.items():
            if v == 0: queue.append(k)
        
        while queue:
            curr = queue.popleft()
            for n in neighbours[curr]:
                indegree[n] -= 1
                if indegree[n] == 0: queue.append(n)
            courses+=1
        
        return courses == numCourses
        