class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree, neighbours, courses, order = {}, {}, 0, []
        for j in range(numCourses): indegree[j], neighbours[j] = 0, []
        for i in range(len(prerequisites)):
            dst, src = prerequisites[i]
            indegree[dst] += 1
            neighbours[src].append(dst)
            
        queue = deque()
        for k, v in indegree.items():
            if v == 0: queue.append(k)
                
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for n in neighbours[curr]:
                indegree[n] -= 1
                if indegree[n] == 0: queue.append(n)
            courses+=1
        
        return order if courses == numCourses else []